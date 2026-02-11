# 🚀 Telegram AI Toolkit Bot

A production-ready Telegram bot demonstrating AI integration using **Aiogram + Groq (OpenAI-compatible API) + SQLite**.

This project showcases real backend engineering skills including:

- Telegram bot architecture with aiogram
- LLM API integration (Groq / OpenAI-compatible)
- Per-user state management
- Per-user conversation memory
- SQLite persistence layer
- Rate limiting (anti-spam protection)
- Timeout protection
- Structured logging
- Clean modular architecture

---

## 📌 Features

### 🤖 AI Modes
- 💬 Chat – general AI conversation  
- ✅ Grammar – correct English grammar only  
- 🧾 Summarize – summarize long text  
- 🌐 Translate – Uzbek ↔ English translation  

### 🧠 Smart Memory
- Per-user conversation history stored in SQLite  
- Reset memory option  

### 🛡 Reliability
- Rate limiting (anti-spam protection)  
- Timeout handling (prevents LLM hanging)  
- Structured logging  
- Graceful error handling  

---

## 🏗 Tech Stack

- Python 3.12+
- Aiogram
- Groq LLM (OpenAI-compatible endpoint)
- SQLite (aiosqlite)
- python-dotenv

---

## 📂 Project Structure

```text
src/
│
├── main.py
├── config.py
│
├── handlers/
│   ├── start.py
│   └── chat.py
│
├── services/
│   ├── llm.py
│   ├── rate_limit.py
│   └── logger.py
│
└── storage/
    ├── db.py
    └── repo.py
```

---

## ⚙ Installation

### 1️⃣ Clone repository

```bash
git clone <your-repo-url>
cd aichatbot
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Setup environment variables

Create a `.env` file in project root:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

Or copy from template:

```bash
cp .env.example .env
```

---

## ▶ Running the Bot

```bash
python -m src.main
```

Bot starts in polling mode.

---

## 🧪 Demo Usage

1. Send `/start`
2. Choose a mode
3. Send a message
4. Try:
   - Grammar correction
   - Translation
   - Long text summarization
5. Use **Reset memory**
6. Send 6+ messages quickly → rate limiting activates

---

## 🔌 LLM Configuration

Current model:

```text
llama-3.1-8b-instant
```

Endpoint:

```text
https://api.groq.com/openai/v1
```

You can change the model inside:

```text
src/services/llm.py
```

---

## 🛡 Security

- `.env` is excluded from Git
- API keys are not committed
- `bot.db` is excluded from version control

---

## 🎯 What This Project Demonstrates

- Modular Telegram bot architecture  
- OpenAI-compatible LLM integration  
- Persistent state and memory  
- SQLite backend usage  
- Async execution with timeout protection  
- Production-style error handling  

This repository is suitable for:

- Portfolio showcase  
- Upwork client demonstration  
- AI bot starter template  
- Backend learning reference  

---

## 📄 License

MIT
