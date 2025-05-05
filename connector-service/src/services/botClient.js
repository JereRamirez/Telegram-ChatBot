import fetch from 'node-fetch';
import config from '../config/index.js';

/**
 * Client for interacting with the Bot Service
 */
class BotClient {
    constructor(botUrl = config.botService.url) {
        this.botUrl = botUrl;
    }

    /**
     * Send a message to the bot service
     * @param {string} telegramId - User's Telegram ID
     * @param {string} messageText - Message text from the user
     * @returns {Promise<Object>} - Response from the bot service
     */
    async sendMessage(telegramId, messageText) {
        console.log(`Sending message to bot service for user ${telegramId}: ${messageText}`);

        try {
            const response = await fetch(this.botUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    telegram_id: telegramId,
                    message_text: messageText
                }),
            });

            if (!response.ok) {
                throw new Error(`Error from Bot Service: ${response.status} ${response.statusText}`);
            }

            const data = await response.json();
            console.log('Bot service response received');
            return data;
        } catch (error) {
            console.error('Error communicating with bot service:', error);
            throw error;
        }
    }
}

export default BotClient;