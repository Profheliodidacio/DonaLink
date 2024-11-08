import unittest
from src.screens import main_screen

class TestMainScreen(unittest.TestCase):
    def test_screen_rendering(self):
        # Teste básico para verificar se a tela principal é exibida corretamente
        # Aqui você pode simular a renderização e verificar elementos-chave
        self.assertTrue(main_screen.show())
    
    def test_call_to_action(self):
        # Teste para verificar se o botão "Comece a Doar" funciona
        result = main_screen.show()  # Suponha que a função `show()` retorne um estado
        self.assertIn("Comece a Doar", result)
    
if __name__ == '__main__':
    unittest.main()
