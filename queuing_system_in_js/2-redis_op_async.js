import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Promisify the get method
const getAsync = promisify(client.get).bind(client);

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

// Function to display the value of a school from Redis using async/await
async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.log(`Error retrieving value for ${schoolName}: ${err.message}`);
    }
}

// Set the initial value for Holberton
setNewSchool('Holberton', 'School');

// Delay the retrieval to ensure the value is set before trying to get it
setTimeout(async () => {
    await displaySchoolValue('Holberton');
}, 100); // Adjust time as necessary (100ms in this case)

// Set new school value and display it
setNewSchool('HolbertonSanFrancisco', '100');
setTimeout(async () => {
    await displaySchoolValue('HolbertonSanFrancisco');
}, 100); // Adjust time as necessary (100ms in this case)
