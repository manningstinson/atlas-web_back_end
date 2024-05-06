// 2-hbtn_course.js

export default class HolbertonCourse {
	constructor(name, length, students) {
		this.name = name;
		this.length = length;
		this.students = students;
	}

	// Getter and setter for name attribute
	get name() {
		return this.name;
	}

	set name(value) {
		if (typeof value !== "string") {
			throw new TypeError("Name must be a string");
		}
		this.name = value;
	}

	// Getter and setter for length attribute
	get length() {
		return this.length;
	}

	set length(value) {
		if (typeof value !== "number") {
			throw new TypeError("Length must be a number");
		}
		this.length = value;
	}

	// Getter and setter for students attribute
	get students() {
		return this.students;
	}

	set students(value) {
		if (
			!Array.isArray(value) ||
			!value.every((item) => typeof item === "string")
		) {
			throw new TypeError("Students must be an array of strings");
		}
		this.students = value;
	}
}
