// 10-car.js
export default class Car {
	constructor(brand, motor, color) {
		this._brand = brand;
		this._motor = motor;
		this._color = color;
	}

	// Define getter for Symbol.species
	static get [Symbol.species]() {
		// Ensure that cloneCar method returns an instance of the same class it is called on
		return this;
	}

	cloneCar() {
		// Use Symbol.species to create a new instance
		return new this.constructor[Symbol.species](
			this._brand,
			this._motor,
			this._color
		);
	}
}
