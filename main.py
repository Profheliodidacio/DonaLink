import streamlit as st
from src.routes.router import r_show

def main():
    # Inicializa o estado do menu na primeira execução
    if "menu_choice" not in st.session_state:
        st.session_state["menu_choice"] = "Principal"  # Tela padrão inicial

    # Renderiza o roteador que gerencia a navegação
    r_show()

if __name__ == "__main__":
    # Configuração inicial do Streamlit
    st.set_page_config(
        page_title="DonaLink - Doe com Propósito",
        page_icon=":heart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # Inicia o aplicativo
    main()
