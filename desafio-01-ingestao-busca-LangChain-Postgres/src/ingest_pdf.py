import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

load_dotenv()

# -- Iniciando ingestão de PDF na base --------------
def ingest_pdf(pdf_path: str):
    
    print("🚀 Iniciando processamento do PDF...")
    
    doc = _read_pdf(pdf_path)
    chunks = _create_chunks(doc)
    enriched = _enrich_chunks(chunks)
    save_embeddings(enriched)

    print("✅ Processamento do PDF finalizado com sucesso!")
# -------------------- -----------------------------


# -------------------- READ PDF --------------------
def _read_pdf(pdf_path: str) -> str:
    
    print("🚀 Lendo um arquivo pdf com langchain")

    doc = PyPDFLoader(pdf_path).load()
    #print(f"doc:\n{doc}")
    print(f"-> PDF carregado: {len(doc)} páginas")
    return doc
# -------------------- -----------------------------



# -------------------- CHUNKS --------------------
def _create_chunks(docs: list[Document], chunk_size: int = 1000, chunk_overlap: int = 150) -> list[Document]:
    
    print("🚀 Criando chunks para um texto...")
    """
    Divide documentos em chunks menores.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=False
    )
    chunks = splitter.split_documents(docs)

    if not chunks:
        raise SystemExit("Nenhum chunk foi criado.")

    print(f"-> Chunks criados: {len(chunks)}")

    return chunks

# -------------------------------------------------



# -------------------- ENRICHED --------------------
def _enrich_chunks(chunks: list[Document]) -> list[Document]:
    """
    Remove metadados vazios dos chunks.
    """
    enriched = [
        Document(
            page_content=d.page_content,
            metadata={k: v for k, v in d.metadata.items() if v not in ("", None)}
        )
        for d in chunks
    ]
    return enriched

# -------------------------------------------------



# -------------------- EMBEDDINGS --------------------
def save_embeddings(enriched: list[Document]) -> None:
    """
    Cria embeddings e salva os documentos no PGVector.
    """
    embeddings = OpenAIEmbeddings(
        model=os.getenv("OPENAI_MODEL", "text-embedding-3-small")
    )

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME", "default_collection"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

    ids = [f"doc-{i}" for i in range(len(enriched))]
    store.add_documents(documents=enriched, ids=ids)

    print(f"-> {len(enriched)} documentos salvos no PGVector com embeddings.")

# -------------------------------------------------


if __name__ == "__main__":
    ingest_pdf(os.getenv("PDF_PATH"))