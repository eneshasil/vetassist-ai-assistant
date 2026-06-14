import os
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VECTOR_DB_DIR = os.path.join(BASE_DIR, "data", "vector_db")

def get_vetassist_response(user_query):
    llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", api_key = GEMINI_API_KEY, temperature = 0)

    print("\nKullanıcının sorusu taranıyor ve İngilizceye çevriliyor...")
    translate_prompt = ChatPromptTemplate.from_messages([
        ("system", "Sen tıbbi bir çevirmensin. Kullanıcının veterinerlik/radyoloji ile ilgili sorduğu soruyu İngilizceye çevir. Sadece İngilizce çeviriyi yaz, başka hiçbir açıklama yapma."),
        ("human", "{input}")
    ])
    translator_chain = translate_prompt | llm | StrOutputParser()
    english_query = translator_chain.invoke({"input": user_query})
    print(f"Arama için kullanılacak arka plan sorgusu: {english_query}")

    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory=VECTOR_DB_DIR, embedding_function=embedding_model)
    retriever = vector_db.as_retriever(search_kwargs={"k": 4})

    print("Veritabanında ilgili tıbbi sayfalar aranıyor...")
    docs = retriever.invoke(english_query)
    context_text = "\n\n".join([doc.page_content for doc in docs])

    system_prompt = (
        "Sen 'VetAssist' uygulaması için çalışan uzman bir veteriner radyoloji asistanısın. "
        "Sana sağlanan tıbbi röntgen ve ultrason kitabı metinlerini (Context) kullanarak "
        "kullanıcının sorusunu profesyonel ve bilimsel bir dille Türkçe olarak yanıtla. "
        "Eğer sorunun cevabı sana verilen kaynak metinlerde (Context) yoksa, "
        "kesinlikle kendi bilgilerini kullanarak uydurma yapma, sadece 'Bu bilgi mevcut veritabanımda bulunmuyor' de.\n\n"
        "Kaynak Bilgi (Context):\n{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    rag_chain = prompt | llm | StrOutputParser()
    
    answer = rag_chain.invoke({"context": context_text, "input": user_query})

    return {"answer": answer, "context": docs}

if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        soru = input("Lütfen sorunuzu girin (Çıkmak için 'q' veya 'çıkış' yazın): ")
        
        if soru.lower().strip() in ['q', 'çıkış', 'exit']:
            print("VetAssist kapatılıyor. İyi çalışmalar!")
            break
            
        if not soru.strip():
            print("Lütfen geçerli bir soru girin.")
            continue

        print("\nAsistan kitaplarda arama yapıyor ve yanıt hazırlıyor...\n")

        yanit = get_vetassist_response(soru)

        print("--- VETASSIST YANITI ---")
        print(yanit["answer"])
        print("------------------------\n")

        print("Kullanılan Kaynaklar (Şeffaflık için):")
        for doc in yanit["context"]:
            dosya_adi = os.path.basename(doc.metadata.get('source', 'Bilinmeyen Dosya'))
            sayfa = doc.metadata.get('page', 'Bilinmiyor')
            print(f"- {dosya_adi} (Sayfa: {sayfa})")

