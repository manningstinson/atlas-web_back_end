// Import Kue
const kue = require('kue');

// Create a queue
const queue = kue.createQueue();

// Define sendNotification function
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Process jobs from the 'push_notification_code' queue
queue.process('push_notification_code', function(job, done) {
  const { phoneNumber, message } = job.data;
  
  sendNotification(phoneNumber, message);
  
  done(); // Call done() when the job is finished
});
