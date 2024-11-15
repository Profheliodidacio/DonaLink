import streamlit as st

def login_show():
    st.title("Tela de Login")

    username = st.text_input("Nome de usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if username == "admin" and password == "admin":
            st.success("Bem-vindo!")
        else:
            st.error("Credenciais inválidas.")
