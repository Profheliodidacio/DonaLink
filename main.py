from src.main_app import main_app

if __name__ == "__main__":
    main_app()






# import streamlit as st
# from src.routes.router import router_show

# def main_page():
    
        
#     # Configurando o estado inicial    
#     if "menu_choice" not in st.session_state:
#         st.session_state['logged_in'] = False
#         st.session_state["menu_choice"] = "Principal"  # Tela padrão inicial

#     # Renderiza o roteador que gerencia a navegação
#     router_show()
#     # if st.session_state['logged_in']:
#     #     main_page()
#     # else:
#     #     login_show()

# if __name__ == "__main__":
#     # Configuração inicial do Streamlit
#     st.set_page_config(
#         page_title="DonaLink - Doe com Propósito",
#         page_icon=":heart:",
#         layout="wide",
#         initial_sidebar_state="expanded",
#     )
#     # Inicia o aplicativo
#     main_page()


# Função para a tela principal
# def main_page():
#     st.title("Tela Principal")
#     st.write("Bem-vindo à aplicação!")
#     if st.button("Sair"):
#         st.session_state['logged_in'] = False
#         st.experimental_rerun()

# Configurando o estado inicial
# if 'logged_in' not in st.session_state:
#     st.session_state['logged_in'] = False

# Lógica para exibir a tela apropriada
# if st.session_state['logged_in']:
#     main_page()
# else:
#     login_show()