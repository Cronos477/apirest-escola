from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status

class AuthenticationTestCase(APITestCase):
    def setUp(self) -> None:
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        
    def test_athentication_ok(self):
        """
            Teste para verificação de credenciais ok
        """
        usuario = authenticate(username='admin', password='admin')
        self.assertTrue((usuario) and usuario.is_authenticated)

    def test_athentication_not_ok(self):
        """
            Teste para verificação de username não ok
        """
        usuario = authenticate(username='adm', password='admin')
        self.assertFalse((usuario) and usuario.is_authenticated)
    
    def test_athentication_pass_ok(self):
        """
            Teste para verificação de password não ok
        """
        usuario = authenticate(username='admin', password='adm')
        self.assertFalse((usuario) and usuario.is_authenticated)
    
    def test_get_auth(self):
        """
            Testa se a GET request é authorizada
        """
        self.client.force_authenticate(self.usuario)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_unauth(self):
        """
            Testa se a GET request não é authorizada
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)