from django.shortcuts import redirect, render, get_object_or_404
from .models import Autor, Libro


def inicio(request):
    return redirect('lista_autores')


def lista_autores(request):
    autores = Autor.objects.all().order_by('nombre')
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def lista_libros(request):
    libros = Libro.objects.select_related('autor').all().order_by('titulo')
    return render(request, 'gestion/lista_libros.html', {'libros': libros})


#Eliminar autor
def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)

    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')

    return render(request, 'gestion/autor_confirm_delete.html', {'autor': autor})


#Eliminar libro
def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)

    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')

    return render(request, 'gestion/libro_confirm_delete.html', {'libro': libro})