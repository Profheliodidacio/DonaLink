import unittest
from src.routes import router

class TestRouter(unittest.TestCase):

    def test_navigation_to_main_screen(self):
        """Testa se a navegação para a tela principal funciona corretamente"""
        # Simula a navegação para a tela principal
        screen = router.navigate("main")
        self.assertEqual(screen, "main_screen")  # A função de navegação deve retornar 'main_screen'

    def test_navigation_to_login_screen(self):
        """Testa se a navegação para a tela de login funciona corretamente"""
        # Simula a navegação para a tela de login
        screen = router.navigate("login")
        self.assertEqual(screen, "login_screen")  # A função de navegação deve retornar 'login_screen'

    def test_navigation_to_info_screen(self):
        """Testa se a navegação para a tela de informações funciona corretamente"""
        # Simula a navegação para a tela de informações
        screen = router.navigate("info")
        self.assertEqual(screen, "info_screen")  # A função de navegação deve retornar 'info_screen'

    def test_navigation_to_about_screen(self):
        """Testa se a navegação para a tela sobre funciona corretamente"""
        # Simula a navegação para a tela sobre
        screen = router.navigate("about")
        self.assertEqual(screen, "about_screen")  # A função de navegação deve retornar 'about_screen'

    def test_navigation_to_portfolio_screen(self):
        """Testa se a navegação para a tela de portfólio funciona corretamente"""
        # Simula a navegação para a tela de portfólio
        screen = router.navigate("portfolio")
        self.assertEqual(screen, "portfolio_screen")  # A função de navegação deve retornar 'portfolio_screen'

    def test_invalid_navigation(self):
        """Testa se a navegação para uma tela inválida é tratada corretamente"""
        # Simula a navegação para uma tela inexistente
        screen = router.navigate("nonexistent")
        self.assertEqual(screen, "error_screen")  # Se a tela não existir, deve retornar uma tela de erro

if __name__ == '__main__':
    unittest.main()
