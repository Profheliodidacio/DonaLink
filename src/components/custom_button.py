# main_app.py

import streamlit as st
from custom_button import custom_button

def show_main_screen():
    st.header("Bem-vindo ao DonaLink!")
    st.subheader("Facilitando doações para causas sociais")
    
    st.write("Clique no botão abaixo para fazer uma doação e contribuir para uma boa causa.")
    
    # Usando o botão customizado
    if custom_button("Doar Agora", color="#ff4b4b", text_color="white"):
        st.success("Obrigado por sua disposição para doar!")
