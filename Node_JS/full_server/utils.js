import fs from 'fs';

export function readDatabase(filePath) {
    return new Promise((resolve, reject) => {
        fs.readFile(filePath, 'utf8', (err, data) => {
            if (err) {
                return reject(new Error('Cannot load the database'));
            }

            const lines = data.trim().split('\n').slice(1); // Skip the header
            const fields = {};

            lines.forEach(line => {
                const [firstName, , , field] = line.split(',');
                if (!fields[field]) {
                    fields[field] = [];
                }
                fields[field].push(firstName);
            });

            resolve(fields);
        });
    });
}
