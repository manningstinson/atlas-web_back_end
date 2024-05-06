import Currency from './3-currency';

class Pricing {
  constructor(amount, currency) {
    this.amount = null;
    this.currency = null;
    this.setAmount(amount);
    this.setCurrency(currency);
  }

  getAmount() {
    return this.amount;
  }

  setAmount(amount) {
    if (typeof amount !== 'number') {
      throw new TypeError('Amount must be a number');
    }
    this.amount = amount;
  }

  getCurrency() {
    return this.currency;
  }

  setCurrency(currency) {
    if (!(currency instanceof Currency)) {
      throw new TypeError('Currency must be an instance of Currency');
    }
    this.currency = currency;
  }

  displayFullPrice() {
    return `${this.getAmount()} ${this.getCurrency().getName()} (${this.getCurrency().getCode()})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw new TypeError('Amount and conversionRate must be numbers');
    }
    return amount * conversionRate;
  }
}

export default Pricing;
