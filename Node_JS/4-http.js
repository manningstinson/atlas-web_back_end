const http = require('http');

// Create the HTTP server
const app = http.createServer((req, res) => {
    // Set response status code and headers
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    
    // Send the response body
    res.end('Hello Holberton School!');
});

// Make the server listen on port 1245
app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});

// Export the server
module.exports = app;
