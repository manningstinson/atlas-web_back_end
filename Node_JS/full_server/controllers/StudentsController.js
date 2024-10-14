import { readDatabase } from '../utils.js';

export default class StudentsController {
    static async getAllStudents(req, res) {
        const filePath = process.argv[2];
        try {
            const data = await readDatabase(filePath);
            let responseText = 'This is the list of our students\n';

            // Sort the fields alphabetically
            const fields = Object.keys(data).sort((a, b) => a.localeCompare(b));

            fields.forEach(field => {
                responseText += `Number of students in ${field}: ${data[field].length}. List: ${data[field].join(', ')}\n`;
            });

            res.status(200).send(responseText.trim());
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }

    static async getAllStudentsByMajor(req, res) {
        const filePath = process.argv[2];
        const major = req.params.major;

        if (major !== 'CS' && major !== 'SWE') {
            return res.status(500).send('Major parameter must be CS or SWE');
        }

        try {
            const data = await readDatabase(filePath);
            if (!data[major]) {
                res.status(500).send('Cannot load the database');
            } else {
                res.status(200).send(`List: ${data[major].join(', ')}`);
            }
        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}
