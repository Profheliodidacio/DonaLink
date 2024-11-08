# chatbot_api.py

import openai  # Certifique-se de que openai está listado no requirements.txt
import os

# Carregue sua chave de API do OpenAI de uma variável de ambiente
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot_response(user_input):
    """
    Gera uma resposta para o input do usuário usando um modelo de linguagem.
    
    Args:
        user_input (str): A mensagem ou pergunta feita pelo usuário.
    
    Returns:
        str: Resposta gerada pelo chatbot.
    """
    try:
        # Chamada para a API do OpenAI para gerar uma resposta
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente do aplicativo DonaLink, especialista em causas sociais e doações."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        # Extrai a resposta gerada
        chatbot_message = response['choices'][0]['message']['content']
        return chatbot_message

    except Exception as e:
        # Em caso de erro, retorna uma mensagem padrão
        print(f"Erro na API do OpenAI: {e}")
        return "Desculpe, estou tendo dificuldades para responder no momento. Por favor, tente novamente mais tarde."
