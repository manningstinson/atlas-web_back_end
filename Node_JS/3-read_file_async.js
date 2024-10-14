const fs = require('fs').promises;

function countStudents(path) {
    return fs.readFile(path, 'utf8')
        .then((data) => {
            // Split the data by newline to get rows
            const lines = data.trim().split('\n');
            
            if (lines.length === 0) {
                throw new Error('Cannot load the database');
            }

            // Remove the header line
            const students = lines.slice(1).filter(line => line !== '');

            console.log(`Number of students: ${students.length}`);

            const fields = {};

            // Process each student's data
            students.forEach(student => {
                const details = student.split(',');

                const firstName = details[0];
                const field = details[details.length - 1];

                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstName);
            });

            // Log the number of students per field and their names
            for (const field in fields) {
                const studentList = fields[field].join(', ');
                console.log(`Number of students in ${field}: ${fields[field].length}. List: ${studentList}`);
            }
        })
        .catch((error) => {
            throw new Error('Cannot load the database');
        });
}

module.exports = countStudents;
