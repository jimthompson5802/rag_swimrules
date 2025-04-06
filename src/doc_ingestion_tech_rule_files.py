import os
import shutil

from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma.vectorstores import Chroma

RULEBOOK_DIR = "./raw_data/technical_rules"
VECTORDB_DIR = "./db/swim_rules_techrules"
GLOSSARY_FP = "./raw_data/glossary_terms.txt"
GUIDANCE_FP = "./raw_data/interpretation_guidance.txt"


def process_directory(directory_path, text_splitter, vector_store):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)

        loader = TextLoader(file_path, encoding="utf-8")

        documents = loader.load()
        splits = text_splitter.split_documents(documents)
        
        # Add metadata about source file
        for split in splits:
            split.metadata["source_file"] = filename
            split.metadata["page"] = 0
        
        vector_store.add_documents(splits)




def main():

    # Initialize embeddings model
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


    # Configure text splitting glossary terms
    glossary_text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20,
        length_function=len,
    )

    with open(GLOSSARY_FP, "r", encoding="utf-8") as file:
        glossary_text = file.read()

    # configure the interpretation guidance text splitter
    glossary_chunks = glossary_text_splitter.create_documents(
        [glossary_text],
        metadatas=[{"source": GLOSSARY_FP, "page": 0}],
    )

    # with open(GUIDANCE_FP, "r", encoding="utf-8") as file:
    #     stroke_interpretations_text = file.read()

    # stroke_interpretations_chunks = glossary_text_splitter.create_documents(
    #     [stroke_interpretations_text],
    #     metadatas=[{"source": GUIDANCE_FP, "page": 0}],
    # )

    # remove old db
    shutil.rmtree(VECTORDB_DIR, ignore_errors=True)

    # Create vector store with chunks
    vector_store = Chroma.from_documents(
        glossary_chunks, #+ stroke_interpretations_chunks,
        embeddings,
        persist_directory=VECTORDB_DIR
    )

    # Initialize text splitter
    rule_text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    process_directory(RULEBOOK_DIR, rule_text_splitter, vector_store)


    # Example RAG query
    results = vector_store.similarity_search("What is breaststroke", k=3)
    for doc in results:
        print(f"Page {doc.metadata['page']}: {doc.page_content[:100]}...")

if __name__ == "__main__":
    main()