const sinon = require('sinon');
const { expect } = require('chai');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', () => {
  let consoleLogSpy;

  // Hook to run before each test
  beforeEach(() => {
    // Create a spy for console.log
    consoleLogSpy = sinon.spy(console, 'log');
  });

  // Hook to run after each test
  afterEach(() => {
    // Restore the spy after each test
    consoleLogSpy.restore();
  });

  it('should log "The total is: 120" when called with 100 and 20', () => {
    sendPaymentRequestToApi(100, 20);

    // Verify that console.log was called once with the correct message
    expect(consoleLogSpy.calledOnceWithExactly('The total is: 120')).to.be.true;

    // Verify that console.log was called only once
    expect(consoleLogSpy.calledOnce).to.be.true;
  });

  it('should log "The total is: 20" when called with 10 and 10', () => {
    sendPaymentRequestToApi(10, 10);

    // Verify that console.log was called once with the correct message
    expect(consoleLogSpy.calledOnceWithExactly('The total is: 20')).to.be.true;

    // Verify that console.log was called only once
    expect(consoleLogSpy.calledOnce).to.be.true;
  });
});
