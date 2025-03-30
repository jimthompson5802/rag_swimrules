import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma.vectorstores import Chroma

VECTORDB_DIR = "./db/swim_rules_semantic"

# Load PDF with selected pages (e.g., pages 10-15)
loader = PyPDFLoader("raw_data/2025-mini-rulebook.pdf")
pages = loader.load()

# Filter selected pages (0-indexed)
selected_pages = [page for page in pages if 21 <= page.metadata['page'] <= 27]

# Configure text splitting for the pdf technical rules
rule_text_splitter = SemanticChunker(
    OpenAIEmbeddings(model="text-embedding-3-small"),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3,
)

# Split selected pages into chunks
rule_chunks = rule_text_splitter.split_documents(selected_pages)

# Configure text splitting glossary terms
glossary_text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=20,
    length_function=len,
)

with open("./raw_data/glossary_terms.txt", "r", encoding="utf-8") as file:
    glossary_text = file.read()

glossary_chunks = glossary_text_splitter.create_documents(
    [glossary_text],
    metadatas=[{"source": "glossary_terms.txt", "page": 0}],
)

# Initialize embeddings model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# remove old db
shutil.rmtree(VECTORDB_DIR, ignore_errors=True)

# Create vector store with chunks
vector_store = Chroma.from_documents(
    rule_chunks + glossary_chunks,
    embeddings,
    persist_directory=VECTORDB_DIR
)

# Example RAG query
results = vector_store.similarity_search("What is breaststroke", k=3)
for doc in results:
    print(f"Page {doc.metadata['page']}: {doc.page_content[:100]}...")
