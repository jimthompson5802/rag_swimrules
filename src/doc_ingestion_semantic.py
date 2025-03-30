import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from langchain_chroma.vectorstores import Chroma

VECTORDB_DIR = "./db/swim_rules_semantic"

# Load PDF with selected pages (e.g., pages 10-15)
loader = PyPDFLoader("raw_data/2025-mini-rulebook.pdf")
pages = loader.load()

# Filter selected pages (0-indexed)
selected_pages = [page for page in pages if 13 <= page.metadata['page'] <= 27]

# Configure text splitting with overlap
text_splitter = SemanticChunker(
    OpenAIEmbeddings(model="text-embedding-3-small"),
    breakpoint_threshold_type="gradient",
)

# Split selected pages into chunks
chunks = text_splitter.split_documents(selected_pages)

# Initialize embeddings model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# remove old db
shutil.rmtree(VECTORDB_DIR, ignore_errors=True)

# Create vector store with chunks
vector_store = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory=VECTORDB_DIR
)

# Example RAG query
results = vector_store.similarity_search("What is breaststroke", k=3)
for doc in results:
    print(f"Page {doc.metadata['page']}: {doc.page_content[:100]}...")
