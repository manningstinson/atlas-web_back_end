function handleResponseFromAPI(promise) {
  promise
    .then(() => {
      console.log('Got a response from the API');
      return { status: 200, body: 'success' };
    })
    .catch(() => {
      console.log('Got a response from the API');
      return new Error();
    })
    .finally(() => {
      // Additional action can be performed here if needed
    });
}

export default handleResponseFromAPI;
