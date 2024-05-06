const carData = Symbol('carData');

class Car {
  constructor(brand, motor, color) {
    this[carData] = {
      brand,
      motor,
      color,
    };
  }

  get brand() {
    return this[carData].brand;
  }

  get motor() {
    return this[carData].motor;
  }

  get color() {
    return this[carData].color;
  }

  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species(
      this[carData].brand,
      this[carData].motor,
      this[carData].color,
    );
  }

  static get [Symbol.species]() {
    return Car;
  }
}

export default Car;
