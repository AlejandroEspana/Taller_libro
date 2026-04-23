from django.shortcuts import render, get_object_or_404, redirect
from .models import Autor, Libro
from .forms import AutorForm, LibroForm


def inicio(request):
    return render(request, 'inicio.html')


# ──────────────────────────────────────────
#  AUTORES
# ──────────────────────────────────────────

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'lista_autores.html', {'autores': autores})


def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})


def actualizar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'actualizar_autor.html', {'form': form, 'autor': autor})


def eliminar_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        return redirect('lista_autores')
    return render(request, 'eliminar_autor.html', {'autor': autor})


# ──────────────────────────────────────────
#  LIBROS
# ──────────────────────────────────────────

def lista_libros(request):
    libros = Libro.objects.select_related('autor').all()
    return render(request, 'lista_libros.html', {'libros': libros})


def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})


def actualizar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'actualizar_libro.html', {'form': form, 'libro': libro})


def eliminar_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'eliminar_libro.html', {'libro': libro})