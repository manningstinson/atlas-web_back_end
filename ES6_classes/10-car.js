// 10-car.js
export default class Car {
  constructor(brand, motor, color) {
    this.brand = brand;
    this.motor = motor;
    this.color = color;
  }

  // Define getter for Symbol.species
  static get [Symbol.species]() {
    // Ensure that cloneCar method returns an instance of the same class it is called on
    return this;
  }

  cloneCar() {
    // Use Symbol.species to create a new instance
    return new this.constructor[Symbol.species](
      this.brand,
      this.motor,
      this.color,
    );
  }
}
