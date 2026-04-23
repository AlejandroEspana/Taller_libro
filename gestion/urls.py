from django import forms
from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Nombre completo del autor',
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'correo@ejemplo.com',
            }),
            'nacionalidad': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej: Colombiana, Mexicana...',
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'biografia': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Breve biografía del autor...',
                'rows': 4,
            }),
        }
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo electrónico',
            'nacionalidad': 'Nacionalidad',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'biografia': 'Biografía',
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Título del libro',
            }),
            'fecha_publicacion': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'genero': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Ej: Novela, Poesía, Ensayo...',
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '978-XXXXXXXXXX',
            }),
            'autor': forms.Select(attrs={
                'class': 'form-input',
            }),
        }
        labels = {
            'titulo': 'Título',
            'fecha_publicacion': 'Fecha de publicación',
            'genero': 'Género',
            'isbn': 'ISBN',
            'autor': 'Autor',
        }