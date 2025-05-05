import express from 'express';
import TelegramService from '../services/telegram.js';
import BotClient from '../services/botClient.js';

const router = express.Router();
const telegramService = new TelegramService();
const botClient = new BotClient();

/**
 * Handle incoming Telegram webhook requests
 */
router.post('/', async (req, res) => {
    console.log("Received request from Telegram webhook");

    try {
        // Extract message data using the Telegram service
        const messageData = telegramService.parseUpdate(req.body);

        // If there's no valid message, acknowledge and exit
        if (!messageData) {
            console.log("Request doesn't contain a message with text");
            return res.sendStatus(200);
        }

        const { chatId, userId, text } = messageData;
        console.log(`Message from user ${userId}: ${text}`);

        // Forward the message to our Bot Service
        try {
            const botData = await botClient.sendMessage(userId, text);
            console.log('Bot service response:', botData);

            // Send the bot's response back to Telegram if there is one
            if (botData.response) {
                await telegramService.sendMessage(chatId, botData.response);
            }
        } catch (error) {
            // Log the error but don't expose it to the user
            console.error('Error processing message with bot service:', error);
        }
    } catch (error) {
        console.error('Error processing webhook:', error);
    }

    // Always respond to Telegram with 200 OK to acknowledge receipt
    res.sendStatus(200);
});

export default router;