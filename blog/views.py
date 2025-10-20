from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from .models import Post
from .forms import AutorForm, CategoriaForm, PostForm, BusquedaForm

def home(request):
    posts = Post.objects.filter(publicado=True).select_related('autor','categoria')
    form = BusquedaForm(request.GET or None)
    if form.is_valid():
        q = form.cleaned_data.get('q')
        cat = form.cleaned_data.get('categoria')
        if q:
            posts = posts.filter(Q(titulo__icontains=q) | Q(contenido__icontains=q))
        if cat:
            posts = posts.filter(categoria=cat)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj, 'form': form})

def post_detalle(request, pk):
    from .models import Post
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            try:
                autor = form.save()
                messages.success(request, f'¡Autor "{autor.nombre}" creado exitosamente!')
                return redirect('home')
            except Exception as e:
                messages.error(request, f'Error al crear el autor: {str(e)}')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = AutorForm()
    return render(request, 'blog/autor_form.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'blog/categoria_form.html', {'form': form})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
