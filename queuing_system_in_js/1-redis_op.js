import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Function to set a new school value in Redis
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.error(`Error setting value for ${schoolName}: ${err.message}`);
        } else {
            console.log(`Reply: ${reply}`);
        }
    });
}

// Function to display the value of a school from Redis
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, value) => {
        if (err) {
            console.log(`Error retrieving value for ${schoolName}: ${err.message}`);
        } else {
            console.log(value);
        }
    });
}

// Set the initial value for Holberton
setNewSchool('Holberton', 'School');

// Delay the retrieval to ensure the value is set before trying to get it
setTimeout(() => {
    displaySchoolValue('Holberton');
}, 100); // Adjust time as necessary (100ms in this case)

// Set new school value and display it
setNewSchool('HolbertonSanFrancisco', '100');
setTimeout(() => {
    displaySchoolValue('HolbertonSanFrancisco');
}, 100); // Adjust time as necessary (100ms in this case)
