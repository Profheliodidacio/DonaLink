
import streamlit as st

def donate_screen():
    st.title("Faça sua Doação 💖")
    st.image(
        "https://via.placeholder.com/800x300", 
        caption="Junte-se a nós e mude vidas", 
        use_container_width=True
    )

    # Campo para valor da doação
    amount = st.number_input("Digite o valor da doação (em R$):", min_value=0.0, step=10.0)

    # Método de pagamento com ícones
    payment_method = st.radio("Selecione o método de pagamento:", 
                               ["💳 Cartão de Crédito", "⚡ Pix", "📄 Boleto"])

    # Botão de confirmação
    if st.button("Doar"):
        if amount > 0:
            st.success(f"Obrigado por sua doação de R${amount:.2f} via {payment_method}!")
        else:
            st.error("Por favor, insira um valor válido para a doação.")











# import streamlit as st

# def donate_screen():
#     st.title("Faça sua Doação 💖")
#     st.image("https://via.placeholder.com/800x300", caption="Junte-se a nós e mude vidas", use_column_width=True)

#     # Campo para valor da doação
#     amount = st.number_input("Digite o valor da doação (em R$):", min_value=0.0, step=10.0)

#     # Método de pagamento com ícones
#     payment_method = st.radio("Selecione o método de pagamento:", 
#                                ["💳 Cartão de Crédito", "⚡ Pix", "📄 Boleto"])

#     # Botão de confirmação
#     if st.button("Doar"):
#         if amount > 0:
#             st.success(f"Obrigado por sua doação de R${amount:.2f} via {payment_method}!")
#         else:
#             st.error("Por favor, insira um valor válido para a doação.")






# import streamlit as st

# def donate_screen():
#     st.title("Doações")
#     st.write("Ajude-nos a continuar nosso trabalho com sua contribuição!")

#     # Campo para valor da doação
#     amount = st.number_input("Digite o valor da doação (em R$):", min_value=0.0, step=10.0)

#     # Método de pagamento
#     payment_method = st.selectbox("Selecione o método de pagamento:", ["Cartão de Crédito", "Pix", "Boleto"])

#     # Botão de confirmação
#     if st.button("Doar"):
#         if amount > 0:
#             st.success(f"Obrigado por sua doação de R${amount:.2f} via {payment_method}!")
#         else:
#             st.error("Por favor, insira um valor válido para a doação.")
