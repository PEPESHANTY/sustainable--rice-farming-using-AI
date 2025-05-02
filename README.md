# 🌾 Rice Farming Assistance Agent

This AI-powered chatbot helps rice farmers and agricultural professionals get answers to their queries using PDF-based knowledge. It uses **LangChain**, **FAISS**, **OpenAI**, and **Streamlit**, and stores chat history on **AWS S3**.

---

## 🔍 Overview

> 💬 Ask questions in any language – the agent understands and responds using the knowledge extracted from over 30+ rice farming guides in PDF format!

### Key Features:
- 🌐 Multilingual Support (Hindi, Chinese, English, and more)
- 📄 Trained on real-world rice farming PDFs
- 🧠 LangChain + FAISS Vector Search
- 💬 Streamlit UI with live chat
- 💾 Chat history saved & listed via AWS S3
- 🗂️ Sidebar to load past conversations

---

## 📸 Snapshots

### 🔹 PDF Ingestion using FAISS + LangChain

All PDF documents are embedded into vector space using OpenAI and stored using FAISS.


![image](https://github.com/user-attachments/assets/02a40181-16f6-4fb2-831c-9172d8421162)

---

### 🔹 Interactive Chat UI

Chat with the assistant and get real-time responses about rice farming techniques.


![image](https://github.com/user-attachments/assets/6d4227ec-66d9-4e78-94bf-6d35c6658a9f)

---

### 🔹 S3 Chat History Storage

Every session is stored as `.txt` in AWS S3 with timestamps.


![image](https://github.com/user-attachments/assets/046f2780-c3ac-42a3-b159-111b2d46e289)

---

### 🔹 Sidebar with Previous Chats

Easy access to revisit previous interactions from the sidebar dropdown.

![image](https://github.com/user-attachments/assets/758a3f8b-797e-45b2-9b0b-3d4ec07af1f1)

---

## 🧠 How It Works

### 1. PDF Ingestion
- PDFs in the `data/` folder are read and split into chunks.
- `OpenAIEmbeddings` are created via LangChain.
- Vector index is saved to `vectorstore/` using FAISS.

### 2. Query Engine
- User queries are matched against the vectorstore.
- Top matches are used to construct the prompt with context.
- Response is generated via OpenAI and returned to user.

### 3. S3 Chat Logging
- Each conversation is saved to AWS S3 as a `.txt` file.
- Files are auto-timestamped and numbered like `chat_history_3_2025-05-02_07-03-18.txt`.

---

## 🔐 Streamlit Secrets (TOML)

Secrets are stored securely via Streamlit Cloud using TOML format:

```toml
OPENAI_API_KEY = "sk-..."
AWS_ACCESS_KEY_ID = "AKIA..."
AWS_SECRET_ACCESS_KEY = "..."
AWS_DEFAULT_REGION = "eu-north-1"
S3_BUCKET_NAME = "sustainable-rice-chats"
```
## 🌐 Multilingual Support
Interact in multiple languages. The assistant uses OpenAI’s multilingual capabilities to understand and respond in:

🇬🇧 English

🇮🇳 Hindi

🇨🇳 Chinese

🇪🇸 Spanish

🌍 ...and many more

![image](https://github.com/user-attachments/assets/e50413dd-4185-4eff-b74f-f33fd9010427)


## 📁 Project Structure

├── app.py                  # Main Streamlit app
├── scripts/
│   ├── ingest.py           # FAISS ingestion
│   ├── query.py            # RAG logic
│   └── utils.py            # S3 save/load helpers
├── vectorstore/            # FAISS index
├── data/                   # Source PDFs
├── asset/                  # Banner and icons
├── .env / TOML             # Secrets config
├── requirements.txt


## ✅ To Do / Future Ideas
🔊 Add voice-to-text input

📱 Mobile responsive layout

📈 Query analytics dashboard

📢 Local language text-to-speech

## 🙌 Acknowledgements
LangChain

OpenAI API

FAISS by Facebook

Streamlit

Amazon AWS S3

## Built with 💡 by Shantanu Bhute for CeADAR Internship 2025.

