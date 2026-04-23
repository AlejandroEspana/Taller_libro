from django.shortcuts import redirect, render

from .models import Autor, Libro


def inicio(request):
    return redirect('lista_autores')


def lista_autores(request):
    autores = Autor.objects.all().order_by('nombre')
    return render(request, 'gestion/lista_autores.html', {'autores': autores})


def crear_autor(request):
    from .forms import AutorForm

    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()

    return render(request, 'gestion/autor_form.html', {'form': form})


def lista_libros(request):
    libros = Libro.objects.select_related('autor').all().order_by('titulo')
    return render(request, 'gestion/lista_libros.html', {'libros': libros})


def crear_libro(request):
    from .forms import LibroForm

    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()

    return render(request, 'gestion/libro_form.html', {'form': form})
