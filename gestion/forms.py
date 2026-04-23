from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    # Autores
    path('autores/', views.lista_autores, name='lista_autores'),
    path('autores/crear/', views.crear_autor, name='crear_autor'),
    path('autores/<int:pk>/actualizar/', views.actualizar_autor, name='actualizar_autor'),
    path('autores/<int:pk>/eliminar/', views.eliminar_autor, name='eliminar_autor'),

    # Libros
    path('libros/', views.lista_libros, name='lista_libros'),
    path('libros/crear/', views.crear_libro, name='crear_libro'),
    path('libros/<int:pk>/actualizar/', views.actualizar_libro, name='actualizar_libro'),
    path('libros/<int:pk>/eliminar/', views.eliminar_libro, name='eliminar_libro'),
]