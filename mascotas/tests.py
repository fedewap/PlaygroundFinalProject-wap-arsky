
from django.test import TestCase, RequestFactory, Client
from .views import registro
from django.contrib.auth import get_user_model
from .models import mascota
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import form_mascota



class RegistroTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_registro_post(self):
        data = {
            'username': 'usuario1',
        }
        request = self.factory.post('/registro', data)
        respuesta = registro(request)
        self.assertEqual(respuesta.status_code, 200)
        
class PostularViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_postular_view_get(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('postular'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postular.html')
        self.assertIsInstance(response.context['form'], form_mascota)

    def test_postular_view_post(self):
        self.client.force_login(self.user)
        data = {
            'nombre': 'Nombre Mascota',
            'animal': 'Perro',
            'fecha_nacimiento': '2023-01-01',
            'informacion_adicional': 'Información adicional',
        }
        response = self.client.post(reverse('postular'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(mascota.objects.filter(nombre='Nombre Mascota').exists())