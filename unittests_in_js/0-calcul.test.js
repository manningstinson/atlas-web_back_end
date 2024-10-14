// 0-calcul.test.js
const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
    it('should return the sum of rounded numbers', function () {
        assert.strictEqual(calculateNumber(1, 3), 4);
        assert.strictEqual(calculateNumber(1, 3.7), 5);
        assert.strictEqual(calculateNumber(1.2, 3.7), 5);
        assert.strictEqual(calculateNumber(1.5, 3.7), 6);
        assert.strictEqual(calculateNumber(1.4, 3.4), 5);
    });

    it('should handle edge cases', function () {
        assert.strictEqual(calculateNumber(1.5, -1.5), 0);
        assert.strictEqual(calculateNumber(0, 0), 0);
        assert.strictEqual(calculateNumber(-1.5, -1.5), -4);
    });
});
