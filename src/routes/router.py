import streamlit as st
from src.screens import main_screen, login_screen, info_screen, about_screen, portfolio_screen

def show():
    # Cria um menu de navegação
    menu = ["Principal", "Login", "Informações", "Sobre", "Portfólio"]
    choice = st.sidebar.selectbox("Escolha uma tela", menu)

    # Navegação entre as telas com base na escolha
    if choice == "Principal":
        main_screen.show()
    elif choice == "Login":
        login_screen.show()
    elif choice == "Informações":
        info_screen.show()
    elif choice == "Sobre":
        about_screen.show()
    elif choice == "Portfólio":
        portfolio_screen.show()
