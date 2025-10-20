
from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email', 'bio']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']  # slug se autogenera

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'publicado', 'autor', 'categoria']

class BusquedaForm(forms.Form):
    q = forms.CharField(label='Buscar', max_length=100, required=False)
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), required=False, empty_label="Todas las categorías")
