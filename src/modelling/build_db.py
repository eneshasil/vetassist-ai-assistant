import os
import glob
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
VECTOR_DB_DIR = os.path.join(BASE_DIR, "data", "vector_db")

def build_vector_db():
    print(f"Scanning PDF files at data/raw/...")
    pdf_files = glob.glob(os.path.join(RAW_DATA_DIR, "*.pdf"))

    if not pdf_files:
        print(f"Error: No PDF files found in data/raw/ !")
        return

    all_pages = []

    for pdf_path in pdf_files:
        print(f"Reading: {os.path.basename(pdf_path)}")
        try:
            loader = PyPDFLoader(pdf_path)
            pages = loader.load()
            all_pages.extend(pages)
        except Exception as e:
            print(f"Error occured while reading the file: {pdf_path}. Error: {e}")
        
    print(f"\nA total of {len(all_pages)} were saved.")
    print("The texts are being devided into chunks...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        separators = ["\n\n", "\n", ".", " ", ""]
    )
    chunks = text_splitter.split_documents(all_pages)
    print(f"A total of {len(chunks)} chunks were created.")

    print(f"A vector database is being created and saved.")

    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding = embedding_model,
        persist_directory=VECTOR_DB_DIR
    )
    print("All the data has been processed and saved to the AI database.")
    print("Vector Database saved at: {VECTOR_DB_DIR}")

if __name__ == "__main__":
    build_vector_db()


