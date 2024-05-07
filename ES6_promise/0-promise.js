function getResponseFromAPI() {
  return new Promise((resolve, /* unused */ reject) => {
    // Make API call or perform asynchronous task here
    // For demonstration purposes, let's resolve the promise with a sample response
    setTimeout(() => {
      const responseData = { data: 'Sample response from API' };
      resolve(responseData);
    }, 2000); // Simulating a delay of 2 seconds
  });
}

export default getResponseFromAPI;
