const getPaymentTokenFromAPI = require('./6-payment_token');

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
    // Since the function does nothing on failure, we can just resolve it to complete the test
    getPaymentTokenFromAPI(false)
      .then((response) => {
        // Ensure that response is undefined (or handle it as per requirement)
        expect(response).to.be.undefined; // Expect no response
        done(); // Indicate that the test is complete
      })
      .catch((error) => {
        done(error); // Fail the test if there's an error
      });
  });
});
