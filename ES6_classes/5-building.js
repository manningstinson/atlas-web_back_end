class Building {
  constructor(sqft) {
    this.sqft = null;
    this.setSqft(sqft);
  }

  getSqft() {
    return this.sqft;
  }

  setSqft(sqft) {
    if (typeof sqft !== 'number') {
      throw new TypeError('Sqft must be a number');
    }
    this.sqft = sqft;
  }

  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    throw new Error(
      'Class extending Building must override evacuationWarningMessage',
    );
  }
}

export default Building;
