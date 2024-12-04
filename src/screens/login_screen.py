
import streamlit as st

def login_screen():
    st.title("Tela de Login")

    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if username == "admin" and password == "admin123":
            st.success("Login bem-sucedido!")
            st.session_state["logged_in"] = True
            st.rerun()  # Atualiza a interface para exibir o menu
        else:
            st.error("Credenciais inválidas.")












# import streamlit as st

# from main import main_page

# def login_show():
#     st.title("Tela de Login")

#     username = st.text_input("Nome de usuário")
#     password = st.text_input("Senha", type="password")

#     if st.button("Entrar"):
#         if username == "admin" and password == "admin123":
#             st.success("Bem-vindo!")
#             main_page()
#         else:
#             st.error("Credenciais inválidas.")

# Depois de logar, quero direcionar para a tela principal


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