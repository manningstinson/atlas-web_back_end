import kue from 'kue';

// Create the queue
const queue = kue.createQueue();

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

/**
 * Sends notification to a phone number
 * @param {string} phoneNumber - The phone number to send notification to
 * @param {string} message - The message to send
 * @param {Object} job - The kue job object
 * @param {Function} done - Callback to be called when job is complete
 */
function sendNotification(phoneNumber, message, job, done) {
  // Track initial progress
  job.progress(0, 100);

  // Check if number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track progress to 50%
  job.progress(50, 100);

  // Log the notification
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Complete the job
  done();
}

// Process jobs from the push_notification_code_2 queue
// Process 2 jobs at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});