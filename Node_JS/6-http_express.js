const express = require('express');

// Create an instance of an Express app
const app = express();

// Define a route for the root URL ("/")
app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

// Set the app to listen on port 1245
app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});

// Export the app
module.exports = app;
