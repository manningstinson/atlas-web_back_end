import { readDatabase } from '../utils.js';

class StudentsController {
    static async getAllStudents(req, res) {
        try {
            const students = await readDatabase('../database.csv'); // Go up one level to access the CSV file
            const fields = Object.keys(students).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));

            let response = 'This is the list of our students\n';
            response += `Number of students: ${fields.reduce((total, field) => total + students[field].length, 0)}\n`;

            fields.forEach(field => {
                response += `Number of students in ${field}: ${students[field].length}. List: ${students[field].join(', ')}\n`;
            });

            res.status(200).send(response);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const major = req.params.major;

        if (!['CS', 'SWE'].includes(major)) {
            return res.status(500).send('Major parameter must be CS or SWE');
        }

        try {
            const students = await readDatabase('../database.csv'); // Go up one level to access the CSV file
            const fieldStudents = students[major] || [];
            res.status(200).send(`List: ${fieldStudents.join(', ')}`);
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}

export default StudentsController;
