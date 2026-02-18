from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('autor/nuevo/', views.crear_autor, name='crear_autor'),
    path('post/nuevo/', views.crear_post, name='crear_post'),
    path('comentario/nuevo/', views.crear_comentario, name='crear_comentario'),
    path('buscar/', views.buscar_post, name='buscar_post'),

]
