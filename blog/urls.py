
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detalle, name='post_detalle'),
    path('crear/autor/', views.crear_autor, name='crear_autor'),
    path('crear/categoria/', views.crear_categoria, name='crear_categoria'),
    path('crear/post/', views.crear_post, name='crear_post'),
]
