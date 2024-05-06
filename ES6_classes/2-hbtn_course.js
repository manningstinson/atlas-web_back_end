class Course {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Getter and setter for name
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value === 'string') {
      this._name = value;
    } else {
      throw new TypeError('Name must be a string');
    }
  }

  // Getter and setter for length
  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value === 'number') {
      this._length = value;
    } else {
      throw new TypeError('Length must be a number');
    }
  }

  // Getter and setter for students
  get students() {
    return this._students;
  }

  set students(value) {
    if (Array.isArray(value) && value.every((s) => typeof s === 'string')) {
      this._students = value;
    } else {
      throw new TypeError('Students must be an array of strings');
    }
  }
}

// Example usage
const c1 = new Course('Python', 8, ['Alice', 'Bob']);
console.log(c1.name); // Output: Python
c1.name = 'Java'; // Change name
console.log(c1.name); // Output: Java

try {
  c1.name = 10; // Throws TypeError
} catch (error) {
  console.error(error.message); // Output: Name must be a string
}

try {
  const c2 = new Course('JavaScript', '7', ['Alice', 'Bob']); // Throws TypeError
} catch (error) {
  console.error(error.message); // Output: Length must be a number
}
