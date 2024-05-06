import Building from './5-building';

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = null;
    this.setFloors(floors);
  }

  get floors() {
    return this.floors;
  }

  setFloors(floors) {
    if (typeof floors !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    this.floors = floors;
  }

  // eslint-disable-next-line class-methods-use-this
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}

export default SkyHighBuilding;
