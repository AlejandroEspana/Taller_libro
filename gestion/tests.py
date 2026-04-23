from django.test import TestCase
from django.urls import reverse

from .models import Autor, Libro


class GestionCrudTests(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(
            nombre='Gabriel Garcia Marquez',
            correo='gabriel@example.com',
            nacionalidad='Colombiana',
            fecha_nacimiento='1927-03-06',
            biografia='Autor colombiano.',
        )
        self.libro = Libro.objects.create(
            titulo='Cien anos de soledad',
            fecha_publicacion='1967-05-30',
            genero='Novela',
            isbn='9780307474728',
            autor=self.autor,
        )

    def test_listas_cargan(self):
        self.assertEqual(self.client.get(reverse('lista_autores')).status_code, 200)
        self.assertEqual(self.client.get(reverse('lista_libros')).status_code, 200)

    def test_crear_autor(self):
        response = self.client.post(
            reverse('crear_autor'),
            {
                'nombre': 'Laura Restrepo',
                'correo': 'laura@example.com',
                'nacionalidad': 'Colombiana',
                'fecha_nacimiento': '1950-01-01',
                'biografia': 'Escritora colombiana.',
            },
        )

        self.assertRedirects(response, reverse('lista_autores'))
        self.assertTrue(Autor.objects.filter(correo='laura@example.com').exists())

    def test_actualizar_libro(self):
        response = self.client.post(
            reverse('actualizar_libro', args=[self.libro.pk]),
            {
                'titulo': 'El coronel no tiene quien le escriba',
                'fecha_publicacion': '1961-01-01',
                'genero': 'Novela',
                'isbn': self.libro.isbn,
                'autor': self.autor.pk,
            },
        )

        self.assertRedirects(response, reverse('lista_libros'))
        self.libro.refresh_from_db()
        self.assertEqual(self.libro.titulo, 'El coronel no tiene quien le escriba')

    def test_eliminar_autor(self):
        response = self.client.post(reverse('eliminar_autor', args=[self.autor.pk]))

        self.assertRedirects(response, reverse('lista_autores'))
        self.assertFalse(Autor.objects.filter(pk=self.autor.pk).exists())
