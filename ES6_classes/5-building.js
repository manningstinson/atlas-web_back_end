// 5-main.js
import Building from "./5-building.js";

class TestBuilding extends Building {
	// Override the abstract method
	evacuationWarningMessage() {
		// Provide a custom implementation here
		return "Custom evacuation warning message";
	}
}

test("Building forces override", () => {
	expect(() => {
		new TestBuilding(200);
	}).toThrowError(
		"Class extending Building must override evacuationWarningMessage"
	);
});
