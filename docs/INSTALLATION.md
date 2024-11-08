# Guia de Instalação - DonaLink

Este guia explica como instalar e configurar o projeto **DonaLink**, um aplicativo de doação de causas sociais. Siga as etapas abaixo para configurar o ambiente e iniciar o projeto.

---

## Índice

1. [Pré-requisitos](#pré-requisitos)
2. [Clonando o Repositório](#clonando-o-repositório)
3. [Instalando Dependências](#instalando-dependências)
4. [Configuração de Variáveis de Ambiente](#configuração-de-variáveis-de-ambiente)
5. [Inicializando o Aplicativo](#inicializando-o-aplicativo)
6. [Executando Testes](#executando-testes)
7. [Problemas Comuns](#problemas-comuns)

---

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- **Python 3.8 ou superior**
- **Git**
- **Virtualenv** (opcional, mas recomendado)

## Clonando o Repositório

Para começar, clone o repositório do **DonaLink**:

```bash
git clone https://github.com/seu-usuario/DonaLink.git
cd DonaLink

```

## Instalando Dependências
Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash

# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual (Linux/MacOS)
source venv/bin/activate

# Ativar o ambiente virtual (Windows)
.\venv\Scripts\activate

```
Com o ambiente virtual ativado, instale as dependências listadas no requirements.txt:

```bash

pip install -r requirements.txt

```
## Configuração de Variáveis de Ambiente
O DonaLink utiliza algumas variáveis de ambiente para configurar a API do chatbot e outros componentes. Crie um arquivo .env na raiz do projeto e adicione as variáveis a seguir:
```bash

# .env

# Chave de API do OpenAI para o chatbot
OPENAI_API_KEY="sua-chave-aqui"

# Configurações adicionais
APP_SECRET_KEY="sua-chave-secreta"

```
Nota: Substitua "sua-chave-aqui" e "sua-chave-secreta" pelos valores apropriados.

## Inicializando o Aplicativo
Após configurar as dependências e variáveis de ambiente, inicie o aplicativo DonaLink:

```bash

# No terminal
streamlit run main.py

```
Isso abrirá o aplicativo no navegador padrão, geralmente em http://localhost:8501.

## Executando Testes
O projeto contém uma estrutura básica de testes. Para executar todos os testes, utilize o comando:

```bash

pytest tests/
Esse comando executará os testes em tests/ e exibirá um relatório dos resultados.

```
## Problemas Comuns
1. Erro de Permissão ao Instalar Dependências
Se encontrar erros de permissão ao executar pip install, tente:

```bash

pip install -r requirements.txt --user

```
2. Erro de API do OpenAI
Verifique se a chave OPENAI_API_KEY está configurada corretamente no .env. Certifique-se de que sua chave do OpenAI está ativa e possui créditos para chamadas.

## Documentação Adicional
Para mais detalhes sobre a API e funcionalidades do DonaLink, consulte os arquivos:

[API_Documentation.md](https://chatgpt.com/c/API_Documentation.md): Documentação completa da API.
[README.md](../README.md): Visão geral do projeto e funcionalidades.
