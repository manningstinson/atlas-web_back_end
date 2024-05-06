class HolbertonCourse {
  constructor(name, length, students) {
    this.name = null;
    this.length = null;
    this.students = null;
    this.setName(name);
    this.setLength(length);
    this.setStudents(students);
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

  getLength() {
    return this.length;
  }

  setLength(length) {
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this.length = length;
  }

  getStudents() {
    return this.students;
  }

  setStudents(students) {
    if (!Array.isArray(students)) {
      throw new TypeError('Students must be an array');
    }
    if (!students.every((student) => typeof student === 'string')) {
      throw new TypeError('Each student must be a string');
    }
    this.students = students;
  }
}

export default HolbertonCourse;
