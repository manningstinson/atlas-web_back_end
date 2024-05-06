// 10-car.js
export default class Car {
	constructor(brand, motor, color) {
		this._brand = brand;
		this._motor = motor;
		this._color = color;
	}

	// Define getter for Symbol.species
	static get [Symbol.species]() {
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
