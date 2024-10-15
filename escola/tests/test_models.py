from django.test import TestCase
from escola.models import *

class ModelEstudante(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome='Teste',
            email='teste@gmail.com',
            cpf='31276742010',
            data_nascimento='2002-01-01',
            celular='99 99999-9999'
        )

    def test_estudante(self):
        """
            Verifica atributos do modelo de Estudante
        """
        self.assertEqual(self.estudante.nome, 'Teste')
        self.assertEqual(self.estudante.email, 'teste@gmail.com')
        self.assertEqual(self.estudante.cpf, '31276742010')
        self.assertEqual(self.estudante.data_nascimento, '2002-01-01')
        self.assertEqual(self.estudante.celular, '99 99999-9999')