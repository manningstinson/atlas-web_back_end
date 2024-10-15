const express = require('express');
const app = express();
const port = 7865;

app.use(express.json()); // Middleware to parse JSON bodies

app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

// Existing endpoint
app.get('/', (req, res) => {
  res.send('Welcome to the payment system');
});

// New endpoint for available payments
app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false,
    },
  });
});

// New endpoint for login
app.post('/login', (req, res) => {
  const { userName } = req.body;
  res.send(`Welcome ${userName}`);
});

module.exports = app; // Exporting the app for testing
