# Expense Bot Service

A Python-based bot service that analyzes user messages to automatically extract, categorize, and store expense information. The bot uses natural language processing to identify expense-related messages and categorize them into predefined expense categories.
<br>**_It is configured to use Gemini as the project LLM. To switch to a different one, some minor tweaks are required._**

## Features

- **User Authentication**: Only processes messages from whitelisted Telegram users
- **Expense Detection**: Distinguishes between expense-related messages and casual conversation
- **Automatic Categorization**: Intelligently categorizes expenses into predefined categories
- **Database Integration**: Stores all expense data securely in a database
- **User Feedback**: Confirms successful expense recording with category information

## Expense Categories

The bot automatically categorizes expenses into the following predefined categories:
- Housing
- Transportation
- Food
- Utilities
- Insurance
- Medical/Healthcare
- Savings
- Debt
- Education
- Entertainment
- Other

## Architecture

The service follows a modular architecture:

```
expense-bot-service/
│
├── docker-compose.yml       # Docker Compose configuration
├── Dockerfile               # Docker build instructions
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variable template
├── README.md                # Project documentation
│
└── app/
    ├── __init__.py          # Package initialization
    ├── main.py              # Application entry point
    ├── config.py            # Configuration management
    │
    ├── routes/              # API routes
    │   └── message_router.py # Message handling routes
    │
    ├── services/            # Business logic
    │   ├── user_service.py  # User authentication and management
    │   └── expense_service.py # Expense processing and storage
    │
    ├── db/                  # Database layer
    │   ├── database.py      # Database connection management
    │   ├── models.py        # ORM models
    │   └── repositories.py  # Data access objects
    │
    ├── llm/                 # Natural Language Processing
    │   └── expense_categorizer.py # LLM-based expense categorization
    │
    └── utils/               # Utilities
        ├── exceptions.py    # Custom exceptions
        └── logger.py        # Logging configuration
```

## Installation

### Prerequisites
- Python 3.9+
- PostgreSQL database
- Docker and Docker Compose (optional)

### Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/JereRamirez/Telegram-ChatBot
   cd expense-bot-service
   ```

2. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. Configure your environment variables:
   ```
   # API
   API_PORT=api_port
   
   # PostgreSQL Database configuration
   DB_HOST=db_host
   DB_PORT=db_port    
   DB_USER=db_user
   DB_PASSWORD=db_password
   DB_NAME=db_name
   
   # LLM configuration (configured for AI Studio)
   GEMINI_API_KEY=your_llm_api_key
   ```

### Running with Docker

Build and start the service:
```bash
docker-compose up --build
```

### Running Locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python -m app.main
   ```

## Database Setup

The bot requires a PostgreSQL database with the following tables:

1. **users**: Stores whitelisted Telegram users
   - telegram_id (primary key)
   - username
   - created_at
   - active (boolean)

2. **expenses**: Stores recorded expenses
   - id (primary key)
   - user_id (foreign key to users)
   - amount
   - description
   - category
   - created_at
   - expense_date

To initialize the database:
```bash
# The application will run migrations on startup
# or you can run them manually:
python -m app.db.database init
```

## Usage

### Adding Users to Whitelist

Only whitelisted users can use the bot. Add users to the whitelist through database insertion:

```sql
INSERT INTO users (telegram_id, username, active) VALUES ('your_telegram_id', 'your_username', true);
```

### Recording Expenses

Send messages to the bot with expense information. Examples:

- "Paid $50 for groceries yesterday"
- "Spent 120€ on electricity bill"
- "25.50 for lunch today"

### Bot Responses

When an expense is successfully recorded, the bot will reply with:
```
[Category] expense added ✅
```

For example:
```
FOOD expense added ✅
```

## API Endpoints

- **POST /api/message**: Endpoint for processing messages
  - body:
  ```json
    {
        "telegram_id":"some_valid_user_id",
        "message_text":"message_to_be_processed"
    }
  ```
    

## Development

## Troubleshooting

Common issues:

1. **Bot not responding to messages**
   - Check if the user is in the whitelist
   - Verify Telegram connector is properly configured
   - Check application logs for errors

2. **Expenses not being categorized correctly**
   - Review the message format sent to the bot
   - Check LLM service configuration
   - Verify expense categorization logic

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework for building APIs
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- [AI Studio](https://aistudio.google.com/app/apikey) 