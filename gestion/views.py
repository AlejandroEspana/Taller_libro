from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm, LibroForm
from .models import Autor, Libro


def inicio(request):
    return redirect('lista_autores')


def lista_autores(request):
    autores = Autor.objects.all().order_by('nombre')
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()

    return render(
        request,
        'gestion/autor_form.html',
        {'form': form, 'titulo': 'Crear autor', 'boton': 'Guardar'},
    )


def actualizar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)

    return render(
        request,
        'gestion/autor_form.html',
        {'form': form, 'titulo': 'Actualizar autor', 'boton': 'Actualizar', 'autor': autor},
    )


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')

    return render(request, 'gestion/autor_confirm_delete.html', {'autor': autor})


def lista_libros(request):
    libros = Libro.objects.select_related('autor').all().order_by('titulo')
    return render(request, 'gestion/lista_libros.html', {'libros': libros})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()

    return render(
        request,
        'gestion/libro_form.html',
        {'form': form, 'titulo': 'Crear libro', 'boton': 'Guardar'},
    )


def actualizar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)

    return render(
        request,
        'gestion/libro_form.html',
        {'form': form, 'titulo': 'Actualizar libro', 'boton': 'Actualizar', 'libro': libro},
    )


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')

    return render(request, 'gestion/libro_confirm_delete.html', {'libro': libro})
