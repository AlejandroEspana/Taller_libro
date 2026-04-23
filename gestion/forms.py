from django import forms

from .models import Autor, Libro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'correo', 'nacionalidad', 'fecha_nacimiento', 'biografia']
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo electronico',
            'nacionalidad': 'Nacionalidad',
            'fecha_nacimiento': 'Fecha de nacimiento',
            'biografia': 'Biografia',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'correo@ejemplo.com'}),
            'nacionalidad': forms.TextInput(attrs={'placeholder': 'Ej: Colombiana'}),
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'biografia': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Breve biografia'}),
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'genero', 'isbn', 'autor']
        labels = {
            'titulo': 'Titulo',
            'fecha_publicacion': 'Fecha de publicacion',
            'genero': 'Genero',
            'isbn': 'ISBN',
            'autor': 'Autor',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder': 'Titulo del libro'}),
            'fecha_publicacion': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'genero': forms.TextInput(attrs={'placeholder': 'Ej: Novela'}),
            'isbn': forms.TextInput(attrs={'placeholder': '978-XXXXXXXXXX'}),
        }
