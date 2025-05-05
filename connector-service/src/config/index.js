import dotenv from 'dotenv';

// Load environment variables from .env file
dotenv.config();

// Configuration object with all environment variables
const config = {
    // Server configuration
    port: process.env.PORT || 8443,
    serverUrl: process.env.SERVER_URL,

    // Telegram configuration
    telegram: {
        token: process.env.TOKEN,
        apiBaseUrl: 'https://api.telegram.org',
        get apiUrl() {
            return `${this.apiBaseUrl}/bot${this.token}`;
        },
        get webhookPath() {
            return `/webhook/${this.token}`;
        },
        get webhookUrl() {
            return `${config.serverUrl}${this.webhookPath}`;
        }
    },

    // Bot service configuration
    botService: {
        url: process.env.BOT_URL || 'http://localhost:8000/api/message'
    },

    // Fetch configuration
    fetch: {
        maxRetries: 5,
        timeoutMs: 10000
    }
};

// Validate required configuration
const validateConfig = () => {
    const required = ['SERVER_URL', 'TOKEN'];
    const missing = required.filter(key => !process.env[key]);

    if (missing.length > 0) {
        throw new Error(`Missing required environment variables: ${missing.join(', ')}`);
    }
};

export { config, validateConfig };

export default config;