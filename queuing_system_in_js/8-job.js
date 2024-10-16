/**
 * Create push notification jobs
 * @param {Array} jobs - Array of job objects containing phoneNumber and message
 * @param {Object} queue - Kue queue instance
 * @throws {Error} - If jobs is not an array
 */
const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobInfo) => {
    const job = queue.create('push_notification_code_3', jobInfo);

    // When job is created
    job
      .on('created', () => {
        console.log(`Notification job created: ${job.id}`);
      })
      // When job is complete
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      })
      // When job fails
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      })
      // When job is making progress
      .on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });

    job.save();
  });
};

export default createPushNotificationsJobs;