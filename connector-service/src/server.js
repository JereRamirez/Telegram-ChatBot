import createApp from './app.js';
import config, { validateConfig } from './config/index.js';
import TelegramService from './services/telegram.js';

/**
 * Initialize the server
 */
const startServer = async () => {
    try {
        // Validate configuration
        validateConfig();

        // Create app
        const app = createApp();

        // Create Telegram service
        const telegramService = new TelegramService();

        // Start server
        const server = app.listen(config.port, async () => {
            console.log('🚀 Connector service running on port', config.port);

            // Set up webhook with Telegram
            try {
                await telegramService.setWebhook();
            } catch (error) {
                console.error('Failed to set webhook:', error);
            }
        });

        // Handle shutdown gracefully
        const gracefulShutdown = () => {
            console.log('Shutting down gracefully...');
            server.close(() => {
                console.log('Server closed');
                process.exit(0);
            });

            // Force close after timeout
            setTimeout(() => {
                console.error('Could not close connections in time, forcefully shutting down');
                process.exit(1);
            }, 10000);
        };

        process.on('SIGTERM', gracefulShutdown);
        process.on('SIGINT', gracefulShutdown);

        return server;
    } catch (error) {
        console.error('Failed to start server:', error);
        process.exit(1);
    }
};

// Start server if this file is run directly
if (process.env.NODE_ENV !== 'test') {
    startServer();
}

export { startServer };