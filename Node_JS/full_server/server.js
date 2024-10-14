import express from 'express';
import router from './routes/index.js';

const app = express();

// Use the router for all routes
app.use('/', router);

// Listen on port 1245
const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

export default app;
