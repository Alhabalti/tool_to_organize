import express from 'express';
import { setRoutes } from './routes/index';
import { configureMiddleware } from './middleware/index';
import { config } from './config/index';

const app = express();
const PORT = config.PORT || 3000;

// Middleware setup
configureMiddleware(app);

// Routes setup
setRoutes(app);

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});