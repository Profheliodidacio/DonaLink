import streamlit as st
from src.screens import login_screen, info_screen, mental_health_screen

def main():
    st.title("Bem-vindo ao DonaLink")

    # Exemplo de navegação entre telas
    menu = ["Login", "Dicas", "Saúde Mental"]
    choice = st.sidebar.selectbox("Escolha uma opção", menu)

    if choice == "Login":
        login_screen.show()
    elif choice == "Dicas":
        info_screen.show()
    elif choice == "Saúde Mental":
        mental_health_screen.show()

if __name__ == "__main__":
    main()
