import os
import shutil

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma.vectorstores import Chroma

# Load PDF with selected pages (e.g., pages 10-15)
loader = PyPDFLoader("raw_data/2025-mini-rulebook.pdf")
pages = loader.load()

# Filter selected pages (0-indexed)
selected_pages = [page for page in pages if 13 <= page.metadata['page'] <= 27]

# Configure text splitting with overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=2000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""],  # Default hierarchy
    length_function=len,
    is_separator_regex=False    
)

# Split selected pages into chunks
chunks = text_splitter.split_documents(selected_pages)

# Initialize embeddings model
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# remove old db
shutil.rmtree("./db/swim_rules", ignore_errors=True)

# Create vector store with chunks
vector_store = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="./db/swim_rules"
)

# Example RAG query
results = vector_store.similarity_search("What is breaststroke", k=3)
for doc in results:
    print(f"Page {doc.metadata['page']}: {doc.page_content[:100]}...")
