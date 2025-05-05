import config from '../config/index.js';
import { fetchWithRetry } from '../utils/fetch.js';

/**
 * Telegram service to handle interactions with the Telegram API
 */
class TelegramService {
    constructor(apiUrl = config.telegram.apiUrl) {
        this.apiUrl = apiUrl;
    }

    /**
     * Set up the webhook with Telegram
     * @returns {Promise<Object>} - Response from Telegram
     */
    async setWebhook() {
        const url = `${this.apiUrl}/setWebhook?url=${config.telegram.webhookUrl}`;
        try {
            const data = await fetchWithRetry(url, { method: 'GET' });
            console.log('Webhook set:', data);
            return data;
        } catch (err) {
            console.error('Failed to set webhook after retries:', err.message);
            throw err;
        }
    }

    /**
     * Send a message to a Telegram chat
     * @param {string|number} chatId - Telegram chat ID
     * @param {string} text - Message text
     * @returns {Promise<Object>} - Response from Telegram
     */
    async sendMessage(chatId, text) {
        if (!text) {
            console.log('No response to send back to user');
            return null;
        }

        console.log(`Sending message to Telegram: ${text}`);
        const url = `${this.apiUrl}/sendMessage`;
        const payload = {
            chat_id: chatId,
            text,
        };

        try {
            const response = await fetchWithRetry(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload),
            });
            console.log('✅ Message sent to Telegram:', response);
            return response;
        } catch (err) {
            console.error('❌ Error sending message to Telegram:', err.message);
            throw err;
        }
    }

    /**
     * Parse a Telegram update object
     * @param {Object} update - Telegram update object
     * @returns {Object|null} - Parsed message data or null if invalid
     */
    parseUpdate(update) {
        const message = update?.message;
        if (!message || !message.text) {
            return null;
        }

        return {
            chatId: message.chat.id,
            userId: message.from.id.toString(),
            text: message.text
        };
    }
}

export default TelegramService;