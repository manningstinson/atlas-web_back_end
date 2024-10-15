import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', () => {
    console.log('Redis client connected to the server');
    subscriber.subscribe('holberton school channel');
});

subscriber.on('error', (err) => {
    console.log('Redis client not connected to the server: ' + err);
});

subscriber.on('message', (channel, message) => {
    console.log(`Received message: ${message}`);
    if (message === 'KILL_SERVER') {
        subscriber.unsubscribe();
        subscriber.quit();
    }
});
