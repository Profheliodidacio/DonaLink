
import streamlit as st
import plotly.express as px

def portfolio_screen():
    st.title("Portfólio 📊")
    st.write("Explore os projetos realizados através do apoio dos nossos doadores!")

    # Gráfico de exemplo: Doações por categoria
    data = {
        "Categorias": ["Educação", "Saúde", "Tecnologia", "Meio Ambiente"],
        "Doações": [50, 70, 30, 40]
    }
    fig = px.bar(data, x="Categorias", y="Doações", title="Doações por Categoria", color="Categorias", height=400)
    st.plotly_chart(fig)

    # Fotos dos projetos
    st.subheader("Projetos Realizados")
    st.image("https://via.placeholder.com/400x200", caption="Irrigação Inteligente")
    st.image("https://via.placeholder.com/400x200", caption="Doações para Educação")
    st.image("https://via.placeholder.com/400x200", caption="Energia Sustentável")












# import streamlit as st

# def portfolio_screen():
#     st.title("Portfólio")
#     st.write("Explore os projetos realizados através do apoio dos nossos doadores!")
    
#     # Projetos de exemplo
#     st.subheader("Projeto 1: Irrigação Inteligente")
#     st.write("Um sistema de irrigação automatizado para comunidades agrícolas.")
#     st.image("https://via.placeholder.com/400x200", caption="Irrigação Inteligente")
    
#     st.subheader("Projeto 2: Doações para Educação")
#     st.write("Fornecimento de materiais escolares para crianças de baixa renda.")
#     st.image("https://via.placeholder.com/400x200", caption="Doações para Educação")
    
#     st.subheader("Projeto 3: Energia Sustentável")
#     st.write("Instalação de painéis solares em áreas de vulnerabilidade.")
#     st.image("https://via.placeholder.com/400x200", caption="Energia Sustentável")
    
    
#     # Exemplo de dados fictícios
#     doacoes = [
#         {"Projeto": "Educação para Todos", "Valor": "R$ 500", "Data": "01/12/2024"},
#         {"Projeto": "Alimentos para Famílias", "Valor": "R$ 300", "Data": "15/11/2024"},
#     ]
    
#     for doacao in doacoes:
#         st.write(f"**{doacao['Projeto']}** - {doacao['Valor']} - {doacao['Data']}")
    
#     # Gráfico simples
#     st.bar_chart([500, 300])  # Exemplo de gráfico de barras para o impacto financeiro
    
    
    
    
    



#     import streamlit as st

# def portfolio_show():
#     st.title("Portfólio de Doações")
    
#     st.write("Veja o impacto das suas doações e como elas estão ajudando a transformar vidas.")
    
#     # Exemplo de dados fictícios
#     doacoes = [
#         {"Projeto": "Educação para Todos", "Valor": "R$ 500", "Data": "01/12/2024"},
#         {"Projeto": "Alimentos para Famílias", "Valor": "R$ 300", "Data": "15/11/2024"},
#     ]
    
#     for doacao in doacoes:
#         st.write(f"**{doacao['Projeto']}** - {doacao['Valor']} - {doacao['Data']}")
    
#     # Gráfico simples
#     st.bar_chart([500, 300])  # Exemplo de gráfico de barras para o impacto financeiro
