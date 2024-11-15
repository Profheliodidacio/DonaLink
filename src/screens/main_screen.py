import streamlit as st

def show():
    st.title("Bem-vindo ao DonaLink!")
    st.write("Faça a diferença! Comece agora a contribuir para causas importantes.")

    # Botão "Comece a doar"
    if st.button("Comece a doar"):
        # Atualiza o estado da escolha do menu
        st.session_state["menu_choice"] = "Portfólio"
        # Feedback visual
        st.success("Redirecionando para a área de doações...")
