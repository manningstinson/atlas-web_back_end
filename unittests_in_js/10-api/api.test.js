const request = require('supertest');
const { expect } = require('chai');
const app = require('./api');

describe('API Endpoints', () => {
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
        })
        .end(done);
    });
  });

  describe('POST /login', () => {
    it('should return welcome message with username', (done) => {
      request(app)
        .post('/login')
        .send({ userName: 'Betty' })
        .expect('Content-Type', /text/)
        .expect(200)
        .expect('Welcome Betty')
        .end(done);
    });
  });

  describe('GET /cart/:id', () => {
    it('should return payment methods for cart when id is a number', (done) => {
      request(app)
        .get('/cart/123')
        .expect(200)
        .expect('Payment methods for cart 123')
        .end(done);
    });

    it('should return 404 when id is not a number', (done) => {
      request(app)
        .get('/cart/abc')
        .expect(404)
        .expect('Not Found')
        .end(done);
    });
  });
});
