# main_app.py

import streamlit as st
from screens.login_screen import show_login_screen
from screens.info_screen import show_info_screen
from screens.about_screen import show_about_screen
from screens.portfolio_screen import show_portfolio_screen
from config.settingssettings import APP_NAME, APP_VERSION

# Função para definir o layout e a navegação do app
def main():
    # Título do aplicativo
    st.title(f"{APP_NAME} - {APP_VERSION}")

    # Menu de navegação
    menu = ["Principal", "Login", "Informações", "Sobre", "Portfólio", "Doar"]
    choice = st.sidebar.selectbox("Escolha uma opção", menu)

    # Exibir a tela correspondente à escolha do menu
    if choice == "Principal":
        show_main_screen()
    elif choice == "Login":
        show_login_screen()
    elif choice == "Informações":
        show_info_tips_screen()
    elif choice == "Sobre":
        show_about_screen()
    elif choice == "Portfólio":
        show_portfolio_screen()
    elif choice == "Doar":
        show_donate_screen()

# Tela principal
def show_main_screen():
    st.header("Bem-vindo ao DonaLink!")
    st.subheader("Facilitando doações para causas sociais")
    st.write(
        "No DonaLink, você pode facilmente doar para diversas causas sociais."
        " Escolha uma opção no menu à esquerda para saber mais ou começar a doar!"
    )

# Tela de Doação (apenas exemplo básico)
def show_donate_screen():
    st.header("Faça sua Doação!")
    st.subheader("Escolha o valor da sua doação:")
    donation_value = st.number_input("Valor da Doação", min_value=10.0, max_value=5000.0, value=50.0, step=10.0)
    
    if st.button("Confirmar Doação"):
        st.success(f"Agradecemos sua doação de R${donation_value}! Sua contribuição é muito importante.")

# Iniciar a aplicação
if __name__ == "__main__":
    main()
