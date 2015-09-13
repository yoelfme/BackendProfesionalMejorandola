from django.test import TestCase
from .models import Categoria, Enlace
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class EnlaceTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(titulo='Categoria de prueba')
        self.usuario = User.objects.create_user(username='yoel', password='yoel')

    def test_es_popular(self):
        # si un enlace tiene menos de 11 votos no es popular
        enlace = Enlace.objects.create(titulo='Prueba',
                                       enlace='http://platzi.com',
                                       categoria=self.categoria, usuario=self.usuario)

        self.assertEqual(enlace.votos, 0)
        self.assertFalse(enlace.es_popular())

        # si un enlace tiene mas de 11 votos
        enlace.votos = 20
        enlace.save()

        self.assertEqual(enlace.votos, 20)
        self.assertTrue(enlace.es_popular())

    def test_views(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('about'))
        self.assertEqual(res.status_code, 200)

        res = self.client.get(reverse('enlaces'))
        self.assertEqual(res.status_code, 200)

        self.assertTrue(self.client.login(username='yoel', password='yoel'))

        res = self.client.get(reverse('add'))
        self.assertEqual(res.status_code, 200)
