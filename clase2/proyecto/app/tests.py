from django.test import TestCase
from .models import Categoria, Enlace
from django.contrib.auth.models import User


class EnlaceTest(TestCase):
    def test_es_popular(self):
        # si un enlace tiene menos de 11 votos no es popular
        categoria = Categoria.objects.create(titulo='Categoria de prueba')
        usuario = User.objects.create_user(username='yoel', password='yoel')
        enlace = Enlace.objects.create(titulo='Prueba',
                                       enlace='http://platzi.com',
                                       categoria=categoria, usuario=usuario)

        self.assertEqual(enlace.votos, 0)
        self.assertFalse(enlace.es_popular())

        # si un enlace tiene mas de 11 votos
        enlace.votos = 20
        enlace.save()

        self.assertEqual(enlace.votos, 20)
        self.assertTrue(enlace.es_popular())
