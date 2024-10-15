const request = require('supertest');
const { expect } = require('chai');
const app = require('./api');

describe('API Endpoints', () => {
  // Test for the root endpoint
  describe('GET /', () => {
    it('should return status 200 and a welcome message', (done) => {
      request(app)
        .get('/')
        .expect('Content-Type', /text/)
        .expect(200)
        .expect('Welcome to the payment system')
        .end((err, res) => {
          console.log('Root Endpoint Response:', res.text); // Log the response
          done(err);
        });
    });
  });

  // Test for available payments endpoint
  describe('GET /available_payments', () => {
    it('should return available payment methods', (done) => {
      request(app)
        .get('/available_payments')
        .expect('Content-Type', /json/)
        .expect(200)
        .expect((res) => {
          expect(res.body).to.deep.equal({
            payment_methods: {
              credit_cards: true,
              paypal: false,
            },
          });
          console.log('Available Payments Response:', res.body); // Log the response
        })
        .end(done);
    });
  });

  // Test for login endpoint
  describe('POST /login', () => {
    it('should return welcome message with username', (done) => {
      request(app)
        .post('/login')
        .send({ userName: 'Betty' })
        .expect('Content-Type', /text/)
        .expect(200)
        .expect('Welcome Betty')
        .end((err, res) => {
          console.log('Login Response:', res.text); // Log the response
          done(err);
        });
    });
  });

  // Test for cart endpoint
  describe('GET /cart/:id', () => {
    it('should return payment methods for cart when id is a number', (done) => {
      const id = 124; // Example cart ID
      request(app)
        .get(`/cart/${id}`)
        .expect('Content-Type', /text/)
        .expect(200)
        .expect(`Payment methods for cart ${id}`)
        .end((err, res) => {
          console.log('Cart ID Response:', res.text); // Log the response
          done(err);
        });
    });

    it("should return 404 when id is not a number", (done) => {
      const id = "abc"; // Example invalid cart ID
      request(app)
        .get(`/cart/${id}`)
        .expect(404)
        .expect('Not Found')
        .end((err, res) => {
          console.log('Invalid Cart ID Response:', res.text); // Log the response
          done(err);
        });
    });
  });
});
