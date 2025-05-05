import fetch from 'node-fetch';
import config from '../config/index.js';

/**
 * Sleep for a specified number of milliseconds
 * @param {number} ms - milliseconds to sleep
 * @returns {Promise} - resolves after the specified time
 */
export const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

/**
 * Fetch with automatic retries, timeout, and backoff
 * @param {string} url - URL to fetch
 * @param {Object} options - Fetch options
 * @returns {Promise<Object>} - Parsed JSON response
 * @throws {Error} - If all retries fail
 */
export const fetchWithRetry = async (url, options = {}) => {
    const { maxRetries, timeoutMs } = config.fetch;

    for (let attempt = 1; attempt <= maxRetries; attempt++) {
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), timeoutMs);

        try {
            const res = await fetch(url, {
                ...options,
                signal: controller.signal,
            });

            clearTimeout(timeout);

            if (!res.ok) {
                throw new Error(`HTTP ${res.status} - ${res.statusText}`);
            }

            return await res.json();

        } catch (error) {
            const isLastAttempt = attempt === maxRetries;
            console.error(`Attempt ${attempt} failed for ${url}:`, error.message || error);

            if (isLastAttempt) {
                throw error;
            }

            const backoff = Math.pow(2, attempt) * 1000;
            console.log(`Retrying in ${backoff / 1000}s...`);
            await sleep(backoff);
        }
    }
};

export default { fetchWithRetry, sleep };