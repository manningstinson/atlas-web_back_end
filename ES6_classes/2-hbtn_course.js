class HolbertonCourse {
  constructor(name, length, students) {
    this.name = null;
    this.length = null;
    this.students = null;
    this.setName(name);
    this.setLength(length);
    this.setStudents(students);
  }

  get name() {
    return this.name;
  }

  set name(name) {
    if (typeof name !== 'string' && typeof name !== 'number') {
      throw new TypeError('Name must be a string');
    }
    this.name = name;
  }

  get length() {
    return this.length;
  }

  set length(length) {
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    this.length = length;
  }

  get students() {
    return this.students;
  }

  set students(students) {
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
