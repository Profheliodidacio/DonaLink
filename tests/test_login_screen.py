import unittest
from src.screens import login_screen
import streamlit as st

class TestLoginScreen(unittest.TestCase):
    
    def test_login_screen_rendering(self):
        """Testa se a tela de login é renderizada corretamente"""
        # Simula a renderização da tela de login
        result = login_screen.show()  # Supondo que `show()` seja a função de exibição da tela
        self.assertIn("Login", result)  # Verifica se a palavra 'Login' aparece na tela

    def test_login_form_elements(self):
        """Testa se os elementos do formulário de login estão presentes"""
        # Verifica se os campos de entrada existem
        result = login_screen.show()
        self.assertIn("Nome de usuário", result)  # Verifica se o campo 'Nome de usuário' está presente
        self.assertIn("Senha", result)  # Verifica se o campo 'Senha' está presente
        self.assertIn("Entrar", result)  # Verifica se o botão 'Entrar' está presente
    
    def test_valid_login(self):
        """Testa se o login funciona com credenciais válidas"""
        # Simula a ação de login com credenciais válidas
        # (Este teste assume que a função de login é simples e que você pode passar uma credencial mockada)
        user = "doe@exemplo.com"
        password = "senha123"
        
        # Supondo que a função de login retorne uma resposta indicando sucesso
        response = login_screen.login(user, password)  # login() simula a lógica de login
        self.assertTrue(response)  # Se o login for bem-sucedido, a resposta deve ser True
    
    def test_invalid_login(self):
        """Testa o comportamento do login com credenciais inválidas"""
        # Simula a ação de login com credenciais inválidas
        user = "doe@exemplo.com"
        password = "senhaErrada"
        
        # Supondo que a função de login retorne uma resposta indicando falha
        response = login_screen.login(user, password)
        self.assertFalse(response)  # Se o login falhar, a resposta deve ser False

if __name__ == '__main__':
    unittest.main()
