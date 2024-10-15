const getPaymentTokenFromAPI = require('./6-payment_token');
const { expect } = require('chai');

describe('getPaymentTokenFromAPI', () => {
  it('should return a successful response when success is true', (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        // Verify the response
        expect(response).to.deep.equal({ data: 'Successful response from the API' });
        done(); // Indicate that the test is complete
      })
      .catch((error) => {
        done(error); // Fail the test if there's an error
      });
  });

  it('should do nothing when success is false', (done) => {
    const promise = getPaymentTokenFromAPI(false);
    
    // Set a timeout for the test
    const timeoutId = setTimeout(() => {
      done(); // Test passes if the promise does not resolve or reject
    }, 100); // Set a short timeout

    // Since the promise should not resolve, we clear the timeout to avoid false positives
    promise.finally(() => {
      clearTimeout(timeoutId); // Ensure the timeout does not trigger if the promise resolves
    });
  });
});
