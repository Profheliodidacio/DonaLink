import streamlit as st

def show():
    st.title("Sobre o DonaLink")
    
    st.header("Nossa Missão")
    st.write("""
        O DonaLink foi criado para facilitar o processo de doação e engajamento com causas sociais.
        Nosso objetivo é conectar pessoas que desejam ajudar com aquelas que mais precisam.
        Cada doação tem um impacto significativo na vida de muitas pessoas ao redor do mundo.
    """)

    st.header("Nossa Visão")
    st.write("""
        Queremos ser uma plataforma confiável e acessível que incentive a solidariedade e faça
        doações mais transparentes e eficientes. Acreditamos no poder das pequenas ações para
        gerar grandes mudanças.
    """)

    st.header("Como Funciona?")
    st.write("""
        Através do DonaLink, você pode escolher causas que deseja apoiar, fazer doações de maneira
        rápida e segura, e acompanhar o impacto de sua contribuição. Além disso, mostramos a você
        o progresso de cada projeto, garantindo transparência e motivando mais pessoas a se envolverem.
    """)

    st.header("Nosso Compromisso")
    st.write("""
        Estamos comprometidos em promover a solidariedade de forma ética, transparente e inclusiva.
        Nosso trabalho é feito com o apoio de parceiros, voluntários e doadores como você.
        Juntos, podemos fazer do mundo um lugar melhor.
    """)

    st.header("Apoio e Parcerias")
    st.write("""
        O DonaLink conta com a colaboração de diversas ONGs, empresas e indivíduos que compartilham
        da nossa visão. Se você deseja se tornar um parceiro ou apoiar o projeto de outras maneiras,
        entre em contato conosco.
    """)

    # Exemplo de link de contato ou informações extras
    st.markdown("[Entre em contato com a gente!](mailto:contato@donalink.org)")