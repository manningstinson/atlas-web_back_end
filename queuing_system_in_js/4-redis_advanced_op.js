import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Create Hash
const createHash = () => {
    const hashKey = 'HolbertonSchools';
    const locations = {
        Portland: 50,
        Seattle: 80,
        New_York: 20, // Use underscore instead of space for key
        Bogota: 20,
        Cali: 40,
        Paris: 2,
    };

    for (const [city, value] of Object.entries(locations)) {
        client.hset(hashKey, city, value, (err, reply) => {
            if (err) {
                console.error(`Error setting ${city}: ${err.message}`);
            } else {
                console.log(`Reply: OK`); // Log "OK" for successful hset
            }
        });
    }
};

// Display Hash
const displayHash = (hashKey) => {
    client.hgetall(hashKey, (err, obj) => {
        if (err) {
            console.error(`Error retrieving hash: ${err.message}`);
        } else {
            console.log(obj);
        }
    });
};

// Execute the functions
createHash();

// Delay the retrieval to ensure the hash is set before trying to get it
setTimeout(() => {
    displayHash('HolbertonSchools');
}, 100); // Adjust time as necessary (100ms in this case)
