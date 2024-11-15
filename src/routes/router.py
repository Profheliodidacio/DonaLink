import streamlit as st
from src.screens import main_screen, login_screen, info_screen, about_screen, portfolio_screen

def r_show():
    # Inicializa o estado do menu, se necessário
    if "menu_choice" not in st.session_state:
        st.session_state["menu_choice"] = "Principal"

    # Cria um menu de navegação lateral, refletindo o estado atual
    menu = ["Principal", "Login", "Informações", "Sobre", "Portfólio"]
    choice = st.sidebar.selectbox(
        "Escolha uma tela", 
        menu, 
        index=menu.index(st.session_state["menu_choice"])
    )
    
    # Atualiza o estado da sessão com a escolha atual
    st.session_state["menu_choice"] = choice

    # Navega para a tela correspondente
    if st.session_state["menu_choice"] == "Principal":
        main_screen.show()
    elif st.session_state["menu_choice"] == "Login":
        login_screen.login_show()
    elif st.session_state["menu_choice"] == "Informações":
        info_screen.info_show()
    elif st.session_state["menu_choice"] == "Sobre":
        about_screen.about_show()
    elif st.session_state["menu_choice"] == "Portfólio":
        portfolio_screen.portfolio_show()
