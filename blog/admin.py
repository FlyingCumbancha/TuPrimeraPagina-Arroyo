
from django.contrib import admin
from .models import Autor, Categoria, Post

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','email')
    search_fields = ('nombre','email')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','slug')
    prepopulated_fields = {"slug": ("nombre",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','categoria','publicado','fecha_pub')
    list_filter = ('publicado','categoria')
    search_fields = ('titulo','contenido')
