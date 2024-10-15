function getPaymentTokenFromAPI(success) {
  return new Promise((resolve) => {
    if (success) {
      resolve({ data: 'Successful response from the API' });
    }
    // If success is false, we do nothing (no resolve/reject)
  });
}

module.exports = getPaymentTokenFromAPI;
