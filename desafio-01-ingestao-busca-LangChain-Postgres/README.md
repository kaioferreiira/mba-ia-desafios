# 🤖 Assistente IA RAG - Sistema de Busca Semântica com LLM e banco Postgres

<div align="center">
  
  ![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
  ![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green.svg)
  ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-336791.svg)
  ![OpenAI](https://img.shields.io/badge/OpenAI-API-412991.svg)
  ![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)
    

</div>

---

## 📖 Sobre

Este projeto implementa um **Assistente IA com RAG** (Retrieval-Augmented Generation) que permite carregar documentos PDF, processar seu conteúdo e fazer perguntas contextualizadas sobre o material. O sistema utiliza embeddings vetoriais para busca semântica e modelos de linguagem para gerar respostas precisas baseadas apenas no contexto dos documentos carregados.

### ✨ Principais Funcionalidades

- 📄 **Ingestão de Documentos PDF**: Carregamento e processamento automático de arquivos PDF
- 🔍 **Busca Semântica Avançada**: Utiliza embeddings OpenAI para encontrar informações relevantes
- 💬 **Chat Contextualizado**: Respostas baseadas exclusivamente no conteúdo dos documentos
- 🎨 **Interface CLI Interativa**: Terminal colorido e amigável com feedback visual
- 🗄️ **Armazenamento Vetorial**: PostgreSQL com pgvector para persistência eficiente
- ⚡ **Performance Otimizada**: Chunking inteligente e cache de embeddings


## 🚀 Instalação

### Pré-requisitos

- **Python 3.9+**
- **Docker e Docker Compose**
- **Conta OpenAI com API Key**
- **Conta GoogleAI com API Key**

### 📋 Passo a Passo

#### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/kaioferreiira/mba-ia-desafios.git
cd desafio-01-ingestao-busca-LangChain-Postgres
```

#### 2️⃣ Acesse a Pasta do Projeto

```bash
# Navegue até a pasta específica deste projeto
cd desafio-01-ingestao-busca-LangChain-Postgres
```

#### 3️⃣ Configure o Ambiente Virtual

```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente virtual
    # Linux/Mac:
    source venv/bin/activate

    # Windows:
    venv\Scripts\activate

# Desativar ambiente virtual
deactivate
```

#### 4️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

#### 5️⃣ Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (copie do `.env.example` se disponível) com as seguintes variáveis:

```env
GOOGLE_API_KEY=""
GOOGLE_EMBEDDING_MODEL='models/embedding-001'
OPENAI_API_KEY=""
OPENAI_MODEL_CHAT=gpt-3.5-turbo
OPENAI_EMBEDDING_MODEL='text-embedding-3-small'
DATABASE_URL=postgresql://postgres:postgres@127.0.0.1:5432/rag
PG_VECTOR_COLLECTION_NAME=collection_documents_prompts
PDF_PATH="PASTA LOCAL CONTENDO PDF"

```

> 💡 **Dica**: Obtenha sua API Key em [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

#### 6️⃣ Inicie o Banco de Dados

```bash
# Iniciar PostgreSQL com pgvector
sudo docker compose up -d

# Verificar se está rodando
sudo docker compose ps
```
> 💡 **Dica**: Ao rodar o comando compose, pode ser que ja exista algumas instancias docker com a imagem, para não gerar conflitos e criar uma ambiente do zero rode os comandos a seguir para excluir as imagens existentes, e na sequencia execute o compose novamnte. 

```bash
# stop em todas as imagens
sudo docker stop $(sudo docker ps -a -q)

# remover todas as imagens
sudo docker rm $(sudo docker ps -a -q)
```



## 🎮 Como Usar

### Iniciando o Assistente

```bash
python src/chat.py
```

### Interface em Execução

## Execução sem a carga de dados do  PDF

O arquivo ingest_pdf é responsável por realizar a leitura e fazer a carga no banco de dados Postgress vetorial.
Ao executar o chat sem a carga o assistente deverá responder que não pode ajudar.

![Execução sem a carga](exe-sem-dados-na-base.png)


## Execução com a carga de dados do  PDF

![Execução com a carga](exe-com-dados-na-base.png)


## 🛠️ Stack Tecnológica

### Core
- **[LangChain](https://langchain.com/)** (v0.3.27) - Framework para aplicações LLM
- **[OpenAI API](https://openai.com/)** - Embeddings e modelo de linguagem
- **[PostgreSQL](https://www.postgresql.org/)** (v17) - Banco de dados principal
- **[pgvector](https://github.com/pgvector/pgvector)** - Extensão para busca vetorial

### Bibliotecas Python
- **langchain-openai** - Integração com OpenAI
- **langchain-postgres** - Integração com PostgreSQL/pgvector
- **pypdf** - Processamento de arquivos PDF
- **python-dotenv** - Gerenciamento de variáveis de ambiente
- **psycopg** - Driver PostgreSQL para Python

## 🔧 Configurações Avançadas

### Ajuste de Parâmetros

Você pode ajustar os seguintes parâmetros no código:

**Em `ingest.py`:**
```python
# Tamanho dos chunks de texto
chunk_size=1000  # Padrão: 1000 caracteres
chunk_overlap=150  # Padrão: 150 caracteres de sobreposição
```

**Em `search.py`:**
```python
# Número de chunks relevantes para contexto
k=10  # Padrão: 10 chunks mais similares
```

**Em `chat.py`:**
```python
# Modelo e temperatura
temperature=0.5  # Criatividade das respostas (0-1)
```

