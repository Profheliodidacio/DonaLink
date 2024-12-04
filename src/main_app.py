# main_app.py

import streamlit as st
from src.screens.donate_screen import donate_screen
from src.screens.login_screen import login_screen
from src.screens.about_screen import about_screen
from src.screens.portfolio_screen import portfolio_screen

def main_app():
    # Inicializando o estado da sessão
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    # Menu de navegação com emojis
    st.sidebar.title("Menu 📋")
    if st.session_state["logged_in"]:
        menu = st.sidebar.selectbox("Selecione a tela:", [
            "🏠 Doações", 
            "ℹ️ Sobre", 
            "📊 Portfólio", 
            "🚪 Logout"
        ])
        
        if menu == "🏠 Doações":
            donate_screen()
        elif menu == "ℹ️ Sobre":
            about_screen()
        elif menu == "📊 Portfólio":
            portfolio_screen()
        elif menu == "🚪 Logout":
            st.session_state["logged_in"] = False
            st.rerun()
    else:
        login_screen()













# import streamlit as st
# from src.screens.donate_screen import donate_screen
# from src.screens.login_screen import login_screen
# from src.screens.about_screen import about_screen
# from src.screens.portfolio_screen import portfolio_screen

# def main_app():
#     # Inicializando o estado da sessão
#     if "logged_in" not in st.session_state:
#         st.session_state["logged_in"] = False

#     # Menu de navegação
#     st.sidebar.title("Menu")
#     if st.session_state["logged_in"]:
#         menu = st.sidebar.selectbox("Selecione a tela:", ["Doações", "Sobre", "Portfólio", "Logout"])
        
#         if menu == "Doações":
#             donate_screen()
#         elif menu == "Sobre":
#             about_screen()
#         elif menu == "Portfólio":
#             portfolio_screen()
#         elif menu == "Logout":
#             st.session_state["logged_in"] = False
#             st.experimental_rerun()
#     else:
#         login_screen()









# import streamlit as st
# from src.screens.donate_screen import donate_screen
# from src.screens.login_screen import login_screen

# def main_app():
#     # Inicializando o estado da sessão
#     if "logged_in" not in st.session_state:
#         st.session_state["logged_in"] = False

#     # Menu de navegação
#     st.sidebar.title("Menu")
#     if st.session_state["logged_in"]:
#         menu = st.sidebar.selectbox("Selecione a tela:", ["Doações", "Logout"])
#         if menu == "Doações":
#             donate_screen()
#         elif menu == "Logout":
#             st.session_state["logged_in"] = False
#             st.experimental_rerun()
#     else:
#         login_screen()


# # import streamlit as st
# # from src.screens.donate import donate_screen
# # from src.screens.login_screen import login_screen

# def main_app():
#     # Inicializando o estado da sessão
#     if "logged_in" not in st.session_state:
#         st.session_state["logged_in"] = False

#     # Menu de navegação
#     st.sidebar.title("Menu")
#     if st.session_state["logged_in"]:
#         menu = st.sidebar.selectbox("Selecione a tela:", ["Doações", "Logout"])
#         if menu == "Doações":
#             donate_screen()
#         elif menu == "Logout":
#             st.session_state["logged_in"] = False
#             st.experimental_rerun()
#     else:
#         login_screen()




















# import streamlit as st
# from main import main_page
# from screens.donate_screen import show_donate_screen
# from screens.login_screen import show_login_screen
# from screens.info_screen import show_info_screen
# from screens.about_screen import show_about_screen
# from screens.portfolio_screen import show_portfolio_screen
# from config.settings import APP_NAME, APP_VERSION

# # Função para definir o layout e a navegação do app
# def main():
#     # Título do aplicativo
#     st.title(f"{APP_NAME} - {APP_VERSION}")

#     # Menu de navegação
#     menu = ["Principal", "Login", "Informações", "Sobre", "Portfólio", "Doar"]
#     choice = st.sidebar.selectbox("Escolha uma opção", menu)

#     # Exibir a tela correspondente à escolha do menu
#     if choice == "Principal":
#         main_page()
#     elif choice == "Login":
#         show_login_screen()
#     elif choice == "Informações":
#         show_info_screen()
#     elif choice == "Sobre":
#         show_about_screen()
#     elif choice == "Portfólio":
#         show_portfolio_screen()
#     elif choice == "Doar":
#         show_donate_screen()

# Tela principal
# def show_main_screen():
#     st.header("Bem-vindo ao DonaLink!")
#     st.subheader("Facilitando doações para causas sociais")
#     st.write(
#         "No DonaLink, você pode facilmente doar para diversas causas sociais."
#         " Escolha uma opção no menu à esquerda para saber mais ou começar a doar!"
#     )

# Tela de Doação (apenas exemplo básico)
# def show_donate_screen():
#     st.header("Faça sua Doação!")
#     st.subheader("Escolha o valor da sua doação:")
#     donation_value = st.number_input("Valor da Doação", min_value=10.0, max_value=5000.0, value=50.0, step=10.0)
    
#     if st.button("Confirmar Doação"):
#         st.success(f"Agradecemos sua doação de R${donation_value}! Sua contribuição é muito importante.")

# # Iniciar a aplicação
# if __name__ == "__main__":
#     main()
