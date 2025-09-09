# 🤖 Assistente IA RAG - Sistema de Busca Semântica com LLM e banco Postgres

## Sumário
- [Sobre](#sobre)
- [Principais Funcionalidades](#principais-funcionalidades)
- [Instalação](#instalacao)
- [Como Usar](#como-usar)
- [Stack Tecnológica](#stack-tecnologica)
- [Configurações Avançadas](#configuracoes-avancadas)

## 📖 Sobre <a name="sobre"></a>

Este projeto implementa um **Assistente IA com RAG** (Retrieval-Augmented Generation) que permite carregar documentos PDF, processar seu conteúdo e fazer perguntas contextualizadas sobre o material. 
Utiliza embeddings vetoriais para busca semântica e modelos de linguagem para gerar respostas precisas baseadas no contexto dos documentos carregados.

## ✨ Principais Funcionalidades 
- **Ingestão de Documentos PDF**: Carregamento e processamento automático de arquivos PDF
- **Busca Semântica Avançada**: Embeddings OpenAI para encontrar informações relevantes
- **Chat Contextualizado**: Respostas baseadas exclusivamente no conteúdo dos documentos
- **Interface CLI Interativa**: Terminal colorido e amigável
- **Armazenamento Vetorial**: PostgreSQL com pgvector
- **Performance Otimizada**: Chunking inteligente e cache de embeddings

## 🚀 Instalação

### Pré-requisitos
- Python 3.9+
- Docker e Docker Compose
- Conta OpenAI com API Key
- Conta GoogleAI com API Key

### Passo a Passo

1. **Clone o Repositório**
```bash
git clone https://github.com/kaioferreiira/mba-ia-desafios.git
cd desafio-01-ingestao-busca-LangChain-Postgres
```

2. **Acesse a Pasta do Projeto**
```bash
cd desafio-01-ingestao-busca-LangChain-Postgres
```

3. **Configure o Ambiente Virtual**
```bash

# Criar ambiente virtual
python3 -m venv venv

# Linux/Mac:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# Para desativar:
deactivate
```

4. **Instale as Dependências**

```bash
pip install -r requirements.txt
```

5. **Configure as Variáveis de Ambiente**
Crie um arquivo `.env` na raiz do projeto (pode copiar do `.env.example`):

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
> 💡 Obtenha sua API Key em [platform.openai.com/api-keys](https://platform.openai.com/api-keys)

6. **Inicie o Banco de Dados**

```bash
sudo docker compose up -d
sudo docker compose ps
```
> 💡 Se houver conflitos com instâncias Docker existentes, execute:

```bash
sudo docker stop $(sudo docker ps -a -q)
sudo docker rm $(sudo docker ps -a -q)
```

## 🎮 Como Usar <a name="como-usar"></a>

### Iniciando o Assistente

```bash
python src/chat.py
```

### Execução sem a carga de dados do PDF
O arquivo `ingest_pdf` realiza a leitura e carga no banco. Sem a carga, o assistente informará que não pode ajudar.

![Execução sem a carga](exe-sem-dados-na-base.png)

### Execução com a carga de dados do PDF
![Execução com a carga](exe-com-dados-na-base.png)


## 🛠️ Stack Tecnológica <a name="stack-tecnologica"></a>

### Core
- [LangChain](https://langchain.com/) (v0.3.27)
- [OpenAI API](https://openai.com/)
- [PostgreSQL](https://www.postgresql.org/) (v17)
- [pgvector](https://github.com/pgvector/pgvector)

### Bibliotecas Python
- langchain-openai
- langchain-postgres
- pypdf
- python-dotenv
- psycopg


## 🔧 Configurações Avançadas <a name="configuracoes-avancadas"></a>

### Ajuste de Parâmetros

**Em `ingest.py`:**

```python
chunk_size=1000  # Tamanho dos chunks de texto
chunk_overlap=150  # Sobreposição
```

**Em `search.py`:**

```python
k=10  # Número de chunks relevantes
```

**Em `chat.py`:**

```python
temperature=0.5  # Criatividade das respostas (0-1)
```

