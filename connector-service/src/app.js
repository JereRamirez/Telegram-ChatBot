import express from 'express';
import config from './config/index.js';
import webhookRoutes from './routes/webhook.js';
import healthRoutes from './routes/health.js';

/**
 * Create and configure the Express application
 * @returns {Object} - Configured Express app
 */
const createApp = () => {
    const app = express();

    // Middleware
    app.use(express.json());

    // Routes
    app.use(config.telegram.webhookPath, webhookRoutes);
    app.use('/health', healthRoutes);

    return app;
};

export default createApp;