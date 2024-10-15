from escola.serializers import EstudanteSerializer
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from escola.models import Estudante

class EstudantesTestCase(APITestCase):
    def setUp(self) -> None:
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante_01 = Estudante.objects.create(
            nome='Estudante Um',
            email='estudante01@gmail.com',
            cpf='32754178007',
            data_nascimento='2004-01-01',
            celular='99 99999-9999'
        )
        self.estudante_02 = Estudante.objects.create(
            nome='Estudante Dois',
            email='estudante02@gmail.com',
            cpf='28786070070',
            data_nascimento='2004-01-02',
            celular='99 99999-9999'
        )
        
    def test_get_list(self):
        """
            Teste GET
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_get_unique(self):
        """
            Teste GET único
        """
        response = self.client.get(self.url+'1/')
        dados = Estudante.objects.get(pk=1)
        dados_serialized = EstudanteSerializer(instance=dados).data
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, dados_serialized)
    
    def test_post(self):
        """
            Teste POST
        """
        json = {
            'nome': 'Teste',
            'email': 'teste@gmail.com',
            'cpf': '45265534091',
            'data_nascimento': '2000-01-01',
            'celular': '99 99999-9999'
        }
        response = self.client.post(self.url, json)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_delete(self):
        """
            Teste DELETE
        """
        response = self.client.delete(f'{self.url}2/')
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    def test_put(self):
        """
            Teste PUT
        """
        json = {
            'nome':'teste',
            'email':'testeput@gmail.com',
            'cpf':'42370866071',
            'data_nascimento':'2003-05-09',
            'celular':'11 88888-6666'
        }
        response = self.client.put(f'{self.url}1/', data=json)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)