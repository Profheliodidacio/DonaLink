import streamlit as st

def show():
    st.title("Bem-vindo ao DonaLink")
    
    st.header("Sua participação faz a diferença!")
    st.write("Aqui, você pode ajudar a transformar vidas. Descubra as causas que mais precisam de apoio e faça sua doação.")
    
    # Exemplo de chamada para ação
    if st.button("Comece a Doar"):
        st.write("Vamos mostrar as opções de doação disponíveis!")
