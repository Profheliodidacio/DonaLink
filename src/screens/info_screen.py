# info_tips_screen.py

import streamlit as st

# Função para exibir a tela de informações e dicas
def show_info_screen():
    st.header("Informações e Dicas sobre Doações")
    
    st.subheader("Como o DonaLink Funciona?")
    st.write(
        "O DonaLink facilita o processo de doação para diversas causas sociais. "
        "Você pode selecionar uma causa e realizar sua contribuição de forma rápida e segura. "
        "Cada doação é importante e ajuda a promover um impacto positivo na sociedade."
    )
    
    st.subheader("Por Que Doar?")
    st.write(
        "As doações são uma maneira poderosa de apoiar projetos e organizações que estão "
        "fazendo a diferença no mundo. Sua contribuição pode ajudar a melhorar a educação, "
        "a saúde, a qualidade de vida de muitas pessoas e muito mais. "
        "Com o DonaLink, você pode escolher a causa que mais ressoa com seus valores."
    )
    
    st.subheader("Como Funciona o Processo de Doação?")
    st.write(
        "1. Escolha o valor que deseja doar. \n"
        "2. Selecione a causa que você deseja apoiar. \n"
        "3. Complete o processo de pagamento de forma segura. \n"
        "4. Receba um comprovante de doação e a certeza de que sua contribuição está ajudando."
    )
    
    st.subheader("Dicas para Maximizar o Impacto de Sua Doação")
    st.write(
        "Aqui estão algumas dicas para ajudar a tornar sua doação ainda mais impactante:"
    )
    
    st.markdown(
        """
        - **Doações regulares**: Se você puder, considere se tornar um doador regular. Isso ajuda as organizações a planejar e executar projetos de longo prazo.
        - **Pequenas doações, grandes impactos**: Mesmo pequenas quantias podem fazer a diferença quando somadas. Todo valor conta!
        - **Pesquise as causas**: Escolha causas e organizações que compartilham dos seus valores e que são transparentes sobre o uso das doações.
        - **Divulgue a causa**: Espalhe a palavra! Convidar amigos e familiares para participar também pode ajudar a ampliar o impacto da sua doação.
        """
    )
    
    st.subheader("Como Sua Doação Faz a Diferença?")
    st.write(
        "Cada doação ajuda a melhorar as condições de vida, saúde e educação das pessoas beneficiadas."
        " Seu apoio é essencial para projetos que transformam vidas e comunidades inteiras."
    )

    st.image("assets/impact_image.png", caption="O impacto de cada doação", use_column_width=True)
