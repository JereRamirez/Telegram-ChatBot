# 🧠 AI-Powered Telegram Expense Bot

An end-to-end system that processes natural language expense messages from Telegram, extracts structured financial data using LLMs, and persists it for further use.

This project explores what it means to integrate AI as a **core, production-facing component**;not just a development tool focusing on reliability, validation, and system design.

---

## 🚀 Overview

Users can send messages like:

> *“paid 25 usd for dinner with friends”*

The system automatically extracts:
- 💰 Amount  
- 🏷️ Category  
- 📝 Description  

and stores the result in a PostgreSQL database.

Unlike traditional rule-based systems, this project leverages an LLM to handle variability in human language while maintaining production-level safeguards.

---

## 🏗️ Architecture

The system is split into two independent services:

### 🌐 Connector Service (`/connector-service`)
- Node.js (Express)
- Handles Telegram webhook events  
- Forwards user messages to the bot service  
- Implements retry logic for resilient communication  

### 🧠 Expense Bot Service (`/expense-bot-service`)
- Python 3.11 + FastAPI  
- Core processing layer  
- Integrates with LLM (via LangChain)  
- Validates and persists structured data in PostgreSQL  

---

## 🔄 How It Works

1. User sends a message via Telegram  
2. Connector Service receives the webhook event  
3. Message is forwarded to the Bot Service  
4. Bot Service:
   - Validates and preprocesses input  
   - Sends prompt to LLM via LangChain  
   - Extracts structured data (`amount`, `category`, `description`)  
   - Validates the AI response against a schema  
5. Valid data is stored in PostgreSQL  
6. Response is sent back to the user  

---

## 🧠 AI Integration Approach

Instead of treating the LLM as a simple API call, the system is designed with safeguards:

- **Structured prompting** → Enforces consistent JSON outputs  
- **Validation layer** → Treats AI output as untrusted input  
- **Encapsulation** → AI logic is isolated within the service layer  
- **Extensibility** → Easy to swap models or providers  

This ensures the system remains reliable despite the probabilistic nature of LLMs.

---

## ⚙️ Design Principles

- **AI as a bounded dependency**  
  AI is treated like any external system: outputs are validated and never blindly trusted  

- **Separation of concerns**  
  Transport (Telegram), processing (AI), and persistence are decoupled  

- **Production-first mindset**  
  Logging, validation, and error handling are first-class concerns  

- **Modular architecture**  
  Clean separation into routers, services, and repositories  

---

## ⚖️ Trade-offs

| Decision | Trade-off |
|--------|----------|
| Use LLM instead of rules | + Flexibility, - Higher latency |
| Strict validation layer | + Reliability, - Extra processing |
| Decoupled services | + Scalability, - More complexity |

---

## 🧰 Tech Stack

- **Backend (Bot Service)**: FastAPI, Python 3.11  
- **Connector Service**: Node.js, Express  
- **AI Layer**: LangChain + LLM (AI Studio)  
- **Database**: PostgreSQL  
- **Architecture**: Modular (routers, services, repositories)  

---

## 📁 Repository Structure

```
telegram-chatbot/
│
├── expense-bot-service/     # AI processing service (FastAPI)
├── connector-service/       # Telegram webhook handler (Node.js)
└── README.md
```

---

## ▶️ Getting Started

```bash
git clone https://github.com/JereRamirez/Telegram-ChatBot.git
cd Telegram-ChatBot
```

Then follow setup instructions in each service:

- `/expense-bot-service/README.md`  
- `/connector-service/README.md`  

---

## 🔮 Future Improvements

- Retry and fallback strategies for AI failures  
- Response caching for repeated inputs  
- Metrics and observability (latency, success rate, failure rate)  
- Cost optimization across different LLM providers  

---

## 🤝 Contributing

Contributions are welcome. Please:
- Add tests where appropriate  
- Keep code modular and consistent  
- Follow existing structure and conventions  

---

## 📄 License

MIT  

---

## 💡 Why This Project

This project was built to deeply understand the challenges of integrating AI into real systems:
- Handling non-deterministic outputs  
- Designing validation layers  
- Balancing latency vs accuracy  
- Building reliable AI-powered workflows  

It serves as a practical exploration of **AI as part of system design**, not just a development aid.
