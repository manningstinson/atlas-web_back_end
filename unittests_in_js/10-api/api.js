const express = require('express');
const app = express();
const port = 7865;

app.use(express.json()); // Middleware to parse JSON bodies

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

// New endpoint for cart
app.get('/cart/:id', (req, res) => {
  const id = req.params.id;
  if (isNaN(id)) {
    return res.status(404).send('Not Found');
  }
  res.send(`Payment methods for cart ${id}`);
});

// Start the server if this file is run directly
if (require.main === module) {
  app.listen(port, () => {
    console.log(`API available on localhost port ${port}`);
  });
}

module.exports = app; // Exporting the app for testing
