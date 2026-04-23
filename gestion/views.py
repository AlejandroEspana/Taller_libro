from django.shortcuts import redirect, render

from .models import Autor, Libro


def inicio(request):
    return redirect('lista_autores')


def lista_autores(request):
    autores = Autor.objects.all().order_by('nombre')
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def lista_libros(request):
    libros = Libro.objects.select_related('autor').all().order_by('titulo')
    return render(request, 'gestion/lista_libros.html', {'libros': libros})
