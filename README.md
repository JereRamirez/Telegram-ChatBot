# 🧠 Telegram-ChatBot Monorepo
Telegram chatbot that uses LLMs to categorize expenses and persist them in a DB
This monorepo contains two main services for building a Telegram chatbot system:

* [`expense-bot-service`](./expense-bot-service): A Python-based service that processes and categorizes Telegram messages using an LLM and stores data in PostgreSQL.
* [`connector-service`](./connector-service): A Node.js-based service that receives Telegram webhook messages and forwards them to the bot.

---

## 📁 Repository Structure

```
telegram-chatbot/
│
├── expense-bot-service/ # Python bot service
│   ├── app/           # Source code
│   ├── tests/         # Unit tests
│   └── README.md      # Bot-specific README
│
├── connector-service/ # Node.js Telegram connector
│   ├── src/           # Source code
│   ├── tests/         # Unit tests
│   └── README.md      # Connector-specific README
│
└── README.md          # This file
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/JereRamirez/Telegram-ChatBot.git
cd Telegram-ChatBot
```

### 2. Follow README instructions on each component

---

## 🧱 Services Overview

### 🧠 Expense Bot Service (`/expense-bot-service`)

* Python 3.11
* FastAPI backend
* PostgreSQL for persistence
* LLM categorization with LangChain & AI Studio
* Modular structure: routers, services, repositories
* Async and fully tested

📍 Read the [expense-bot-service README](./expense-bot-service/README.md) for full details.

---

### 🌐 Connector Service (`/connector-service`)

* Node.js (ES Modules)
* Express-based Telegram webhook handler
* Forwards messages to bot and relays responses back to Telegram
* Retry logic for resilient HTTP communication
* Health check support

📍 Read the [connector-service README](./connector-service/README.md) for full details.

---

## 🤝 Contributing

Pull requests and issues are welcome. Please include tests where appropriate and follow consistent coding style across both services.

---

## 📄 License

MIT

