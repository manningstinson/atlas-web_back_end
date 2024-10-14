const express = require('express');
const fs = require('fs').promises;

// Function to read the database asynchronously (similar to 3-read_file_async.js)
async function countStudents(path) {
    try {
        const data = await fs.readFile(path, 'utf8');
        const lines = data.trim().split('\n');

        if (lines.length === 0) throw new Error('Cannot load the database');

        const students = lines.slice(1).filter(line => line !== '');

        let output = `Number of students: ${students.length}\n`;
        const fields = {};

        students.forEach(student => {
            const details = student.split(',');
            const firstName = details[0];
            const field = details[details.length - 1];

            if (!fields[field]) {
                fields[field] = [];
            }
            fields[field].push(firstName);
        });

        for (const field in fields) {
            const studentList = fields[field].join(', ');
            output += `Number of students in ${field}: ${fields[field].length}. List: ${studentList}\n`;
        }

        return output.trim();
    } catch (error) {
        throw new Error('Cannot load the database');
    }
}

// Create an instance of an Express app
const app = express();

// Define a route for the root URL ("/")
app.get('/', (req, res) => {
    res.send('Hello Holberton School!');
});

// Define a route for the /students URL
app.get('/students', async (req, res) => {
    const dbPath = process.argv[2]; // Database file path is passed as an argument

    res.setHeader('Content-Type', 'text/plain');
    res.write('This is the list of our students\n');

    try {
        const studentInfo = await countStudents(dbPath);
        res.end(studentInfo);
    } catch (error) {
        res.end(error.message);
    }
});

// Set the app to listen on port 1245
app.listen(1245, () => {
    console.log('Server is listening on port 1245');
});

// Export the app
module.exports = app;
