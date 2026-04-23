from django.urls import path

from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('autores/', views.lista_autores, name='lista_autores'),
    path('libros/', views.lista_libros, name='lista_libros'),
    path('autor/eliminar/<int:pk>/', views.eliminar_autor, name='eliminar_autor'),
    path('libro/eliminar/<int:pk>/', views.eliminar_libro, name='eliminar_libro'),
]
