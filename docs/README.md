
# DonaLink

DonaLink é um aplicativo de doações desenvolvido em Python, criado para conectar doadores com causas sociais em uma plataforma intuitiva e acessível. O objetivo do **DonaLink** é promover o engajamento de doadores, oferecendo uma experiência amigável e motivadora para apoiar projetos em diversas áreas, como educação, saúde, alimentação e habitação.

## Índice

- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Funcionalidades

- **Cadastro e Login de Usuários**: Interface para cadastro seguro e autenticação de usuários.
- **Doações Simples e Seguras**: Permite aos usuários selecionar uma causa e fazer doações de forma rápida e segura.
- **Histórico de Doações**: Cada doador pode visualizar seu histórico de doações e as causas que apoia.
- **Motivação de Engajamento**: Mensagens motivacionais e feedback visual para encorajar contribuições.
- **API de Chatbot**: Integração com um chatbot para responder perguntas frequentes e fornecer informações sobre as causas.

## Tecnologias Utilizadas

- **[Python 3.8+](https://www.python.org/)**: Linguagem principal para desenvolvimento.
- **[Streamlit](https://streamlit.io/)**: Framework para a interface de usuário.
- **[OpenAI API](https://openai.com/api/)**: Integração para o chatbot (opcional).
- **Outros**: Veja `requirements.txt` para dependências adicionais.

## Estrutura do Projeto

```plaintext
DonaLink/
├── assets/                    # Imagens e recursos visuais do app
│   ├── logo.png               # Logo do DonaLink
│   └── default_avatar.png     # Avatar padrão do usuário
├── data/                      # Arquivos de dados para uso do app
│   └── donations_log.json     # Log de doações de exemplo
├── docs/                      # Documentação adicional do projeto
│   └── API_Documentation.md   # Documentação da API de chatbot
├── src/
│   ├── api/                   # API para integração com o chatbot
│   │   └── chatbot_api.py
│   ├── components/            # Componentes reutilizáveis
│   │   ├── custom_button.py
│   │   └── header.py
│   ├── screens/               # Telas do aplicativo
│   │   ├── main_screen.py
│   │   ├── login_screen.py
│   │   ├── info_screen.py
│   │   ├── about_screen.py
│   │   └── portfolio_screen.py
│   ├── routes/                # Controle de navegação entre telas
│   │   └── router.py
│   ├── main_app.py            # Configuração principal do app
├── tests/                     # Testes unitários e de integração
│   ├── test_login_screen.py
│   ├── test_router.py
│   └── __init__.py
├── main.py                    # Arquivo de entrada principal
├── README.md                  # Documentação do projeto
├── requirements.txt           # Lista de dependências do Python
├── config.toml                # Configurações do projeto
└── .gitignore                 # Arquivos ignorados pelo Git
```

## Instalação

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/Profheliodidacio/DonaLink.git
    cd DonaLink
    ```

2. **Crie e ative um ambiente virtual**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate       # No Windows, use .\venv\Scripts\activate
    ```

3. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure as variáveis de ambiente**:

    Crie um arquivo `.env` na raiz do projeto e adicione suas configurações, incluindo a chave do OpenAI para o chatbot, se aplicável:

    ```bash
    OPENAI_API_KEY="sua-chave-aqui"
    APP_SECRET_KEY="sua-chave-secreta"
    ```

## Uso

Inicie o **DonaLink** executando o seguinte comando:

```bash
streamlit run main.py
```

Isso abrirá o aplicativo no navegador, geralmente em [http://localhost:8501](http://localhost:8501).

## Contribuição

Contribuições são bem-vindas! Para contribuir, siga estas etapas:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature-nome-da-feature`).
3. Commit suas alterações (`git commit -am 'Adiciona nova feature'`).
4. Faça o push da branch (`git push origin feature-nome-da-feature`).
5. Abra um Pull Request.

Consulte o `CONTRIBUTING.md` para mais detalhes.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.

---

Obrigado por conferir o **DonaLink**! Esperamos que este projeto ajude a aumentar o engajamento em causas sociais e facilite a conexão entre doadores e projetos importantes.
