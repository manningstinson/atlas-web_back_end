class Currency {
  constructor(code, name) {
    this.code = null;
    this.name = null;
    this.setCode(code);
    this.setName(name);
  }

  getCode() {
    return this.code;
  }

  setCode(code) {
    if (typeof code !== 'string') {
      throw new TypeError('Code must be a string');
    }
    this.code = code;
  }

  getName() {
    return this.name;
  }

  setName(name) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this.name = name;
  }

  displayFullCurrency() {
    return `${this.getName()} (${this.getCode()})`;
  }
}

export default Currency;
