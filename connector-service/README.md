# Connector-Service

A modular Node.js service that connects Telegram with your bot service, acting as a bridge between the Telegram API and your custom bot implementation.

## Features

- **Webhook Integration**: Automatically sets up and handles Telegram webhook
- **Message Processing**: Extracts and forwards messages from Telegram to your bot service
- **Response Handling**: Sends bot responses back to Telegram users
- **Fault Tolerance**: Includes retry mechanisms for API calls
- **Modular Design**: Each component has a single responsibility, making the code easy to maintain and extend

## Architecture

The application follows a modular architecture:

```
/telegram-connector
  /src
    /config         # Configuration module
    /services       # Service modules (Telegram API, Bot Client)
    /utils          # Utility functions (fetch with retry)
    /routes         # Express route handlers
    app.js          # Express app setup
    server.js       # Server entry point
```

### Key Components

- **TelegramService**: Handles all interactions with the Telegram API
- **BotClient**: Communicates with your bot service
- **Express Router**: Manages HTTP endpoints for webhook and health check
- **Fetch Utilities**: Provides robust HTTP request capabilities with retry logic

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/JereRamirez/Telegram-ChatBot
   cd connector-service
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Configuration

Edit the `.env` file with your specific configuration:

```
# Server Configuration
PORT=8443                           # The port your service will run on (must be one of 443, 80, 88, or 8443)
SERVER_URL=https://example.com      # Your server's public URL (ngrok is a valid alternative for testing purposes)

# Telegram Configuration
TOKEN=your_telegram_bot_token       # Your Telegram bot token from BotFather

# Bot Service Configuration
BOT_URL=http://localhost:8000/api/message  # URL of your bot service API
```

## Usage

### Starting the Server

```bash
# Production mode
npm start

# Development mode (with auto-reload)
npm run dev
```

When started, the service will:
1. Set up a webhook with the Telegram API
2. Listen for incoming webhook requests
3. Forward messages to your bot service
4. Send responses back to Telegram users

### API Endpoints

- **Telegram Webhook**: `/webhook/{token}` - Used by Telegram to send updates
- **Health Check**: `/health` - Status endpoint for monitoring

## Flow Diagram

```
┌─────────────┐       ┌───────────────────┐      ┌─────────────┐
│  Telegram   │──────▶│  Connector Service │─────▶│  Bot Service│
│   Server    │◀──────│                    │◀─────│             │
└─────────────┘       └───────────────────┘      └─────────────┘
```

1. User sends a message to your Telegram bot
2. Telegram forwards the message to your connector service via webhook
3. Connector extracts the message and forwards it to your bot service
4. Bot service processes the message and returns a response
5. Connector sends the response back to Telegram
6. Telegram delivers the response to the user

## Error Handling

The service includes robust error handling:

- **API Retries**: Automatically retries failed API calls with exponential backoff
- **Graceful Degradation**: Continues operating even if parts of the system fail
- **Comprehensive Logging**: Detailed logs for debugging

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.