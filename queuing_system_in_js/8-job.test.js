import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

// Test suite for createPushNotificationsJobs
describe('createPushNotificationsJobs', () => {
  let queue;

  // Before running the tests, set up Kue and enter test mode
  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();  // Enter test mode
  });

  // After running the tests, clear the queue and exit test mode
  afterEach(() => {
    queue.testMode.clear();  // Clear the queue after each test
    queue.testMode.exit();   // Exit test mode
  });

  // Test case: it should throw an error if jobs is not an array
  it('should display an error message if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not-an-array', queue)).to.throw(
      'Jobs is not an array'
    );
  });

  // Test case: it should create two new jobs to the queue
  it('should create two new jobs to the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'This is the code 1234' },
      { phoneNumber: '0987654321', message: 'This is the code 5678' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2); // Validate that 2 jobs were added
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]); // Check job 1 data
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]); // Check job 2 data
  });
});
