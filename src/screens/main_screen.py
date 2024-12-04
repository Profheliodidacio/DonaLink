import streamlit as st

def show_main_screen():
    st.title("Bem-vindo ao DonaLink!")
    st.write("Faça a diferença! Comece agora a contribuir para causas importantes.")

    # Botão "Comece a doar"
    if st.button("Comece a doar"):
        # Atualiza o estado da escolha do menu
        st.session_state["menu_choice"] = "Portfólio"
        # Feedback visual
        st.success("Redirecionando para a área de doações...")
        # Inicializa o estado do menu na primeira execução
    if st.button("Sair"):
        st.session_state['logged_in'] = False
        st.experimental_rerun()
