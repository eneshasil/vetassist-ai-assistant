# 🐾 VetAssist AI Assistant

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

**VetAssist AI Assistant**, veteriner hekimler, klinik çalışanları ve evcil hayvan sahipleri için geliştirilmiş, yapay zeka destekli akıllı bir sanal asistandır. Bu proje, hayvan sağlığı süreçlerini hızlandırmak, ön teşhis desteği sağlamak ve hasta kayıt/takip süreçlerini otomatize etmek amacıyla tasarlanmıştır.

## 🚀 Özellikler

- **🤖 Akıllı Soru-Cevap:** Evcil hayvanların semptomlarına ve bakımına dair sık sorulan soruları yapay zeka ile anında yanıtlar.
- **🩺 Ön Teşhis ve Yönlendirme:** Girilen semptomlara dayanarak olası durumlar hakkında bilgi verir ve kritik durumlarda acil veteriner hekim yönlendirmesi yapar.
- **📅 Randevu ve Takip:** Aşı takvimi, ilaç hatırlatıcıları ve klinik randevularının yapay zeka tarafından asiste edilmesi.
- **📁 Klinik Veritabanı Entegrasyonu:** Veteriner hekimler için hasta geçmişine (anamnez) hızlı erişim ve özetleme yeteneği.
- **💬 Doğal Dil İşleme (NLP):** Kullanıcıların karmaşık cümlelerini anlayıp empati kurarak doğru medikal bilgiyi anlaşılır bir dille sunma.

## 🛠️ Kullanılan Teknolojiler

Bu proje geliştirilirken aşağıdaki modern teknolojiler kullanılmıştır:

- **Dil:** Python
- **Yapay Zeka & LLM:** OpenAI API / LangChain / Hugging Face (Kullanılan modele göre özelleştirilebilir)
- **Backend:** FastAPI veya Flask
- **Frontend / Arayüz:** Streamlit veya React.js (Kullanıcı etkileşimi için)
- **Veritabanı:** PostgreSQL / MongoDB veya Vektör Veritabanı (ChromaDB / Pinecone)

## ⚙️ Kurulum

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/eneshasil/vetassist-ai-assistant.git
cd vetassist-ai-assistant
```

### 2. Sanal Ortam (Virtual Environment) Oluşturun
```bash
python -m venv venv
source venv/bin/activate  # Windows için: venv\Scripts\activate
```

### 3. Gerekli Paketleri Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Çevresel Değişkenleri (Environment Variables) Ayarlayın
Proje dizininde bir `.env` dosyası oluşturun ve API anahtarlarınızı ekleyin:
```env
OPENAI_API_KEY=senin_api_anahtarin_buraya
DATABASE_URL=senin_veritabani_url_buraya
```

### 5. Uygulamayı Başlatın
```bash
# Eğer Streamlit kullanılıyorsa:
streamlit run app.py

# Eğer FastAPI/Uvicorn kullanılıyorsa:
uvicorn main:app --reload
```

## 📖 Kullanım

Uygulama çalıştıktan sonra web tarayıcınız üzerinden (genellikle `http://localhost:8501` veya `http://localhost:8000`) asistan ile sohbet arayüzüne erişebilirsiniz. 
Evcil hayvanınızın durumunu, yaşını, cinsini ve belirtilerini yazarak asistandan anında destek alabilirsiniz.

> **⚠️ Yasal Uyarı:** VetAssist AI, yalnızca bilgilendirme amaçlıdır. Profesyonel veteriner hekim muayenesinin, teşhisinin veya tedavisinin yerini almaz. Acil durumlarda daima en yakın veteriner kliniğine başvurun.

## 🤝 Katkıda Bulunma

Bu proje açık kaynaktır ve her türlü katkıya (Pull Request, Issue açma, hata düzeltme, yeni özellik ekleme) açıktır.
1. Projeyi Fork'layın
2. Yeni bir dal (branch) oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit'leyin (`git commit -m 'Yeni bir özellik eklendi'`)
4. Dalınızı (branch) push'layın (`git push origin feature/YeniOzellik`)
5. Bir Pull Request açın

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

## 📬 İletişim

Geliştirici: **eneshasil**
GitHub: [https://github.com/eneshasil](https://github.com/eneshasil)
