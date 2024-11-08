# header.py

import streamlit as st

def show_header():
    """
    Exibe o cabeçalho do aplicativo com logotipo, nome e descrição.
    """
    # Definindo estilo para o cabeçalho
    header_style = """
        <style>
        .header-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.5em 1em;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
        }
        .header-logo {
            width: 50px;
            height: 50px;
            margin-right: 10px;
        }
        .header-text {
            font-size: 24px;
            font-weight: bold;
        }
        .header-description {
            font-size: 14px;
            color: #E5E5E5;
        }
        </style>
    """

    # Exibindo o estilo do cabeçalho no app
    st.markdown(header_style, unsafe_allow_html=True)

    # HTML para o layout do cabeçalho
    header_html = """
    <div class="header-container">
        <div style="display: flex; align-items: center;">
            <img src="assets/logo.png" class="header-logo" alt="Logo DonaLink">
            <div>
                <div class="header-text">DonaLink</div>
                <div class="header-description">Conectando você a causas sociais</div>
            </div>
        </div>
        <div>
            <a href="#doar" style="color: white; font-size: 16px; font-weight: bold; text-decoration: none;">Doar Agora</a>
        </div>
    </div>
    """

    # Renderiza o cabeçalho no aplicativo
    st.markdown(header_html, unsafe_allow_html=True)
