import streamlit as st

def show():
    st.title("Portfólio de Doações")
    
    st.write("Veja o impacto das suas doações e como elas estão ajudando a transformar vidas.")
    
    # Exemplo de dados fictícios
    doacoes = [
        {"Projeto": "Educação para Todos", "Valor": "R$ 500", "Data": "01/12/2024"},
        {"Projeto": "Alimentos para Famílias", "Valor": "R$ 300", "Data": "15/11/2024"},
    ]
    
    for doacao in doacoes:
        st.write(f"**{doacao['Projeto']}** - {doacao['Valor']} - {doacao['Data']}")
    
    # Gráfico simples
    st.bar_chart([500, 300])  # Exemplo de gráfico de barras para o impacto financeiro
