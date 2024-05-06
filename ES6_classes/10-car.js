const carData = Symbol('carData');

class Car {
  constructor(brand, motor, color) {
    this[carData] = {
      brand,
      motor,
      color,
    };
  }

  cloneCar() {
    return new Car(this[carData].brand, this[carData].motor, this[carData].color);
  }
}

export default Car;
