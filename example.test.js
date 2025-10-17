```javascript
const { add, multiply, divide } = require('./example');

describe('Math Operations', () => {
  describe('add()', () => {
    // Test basic addition functionality
    test('should add two positive numbers correctly', () => {
      expect(add(2, 3)).toBe(5);
      expect(add(10, 25)).toBe(35);
    });

    test('should add two negative numbers correctly', () => {
      expect(add(-5, -3)).toBe(-8);
      expect(add(-10, -20)).toBe(-30);
    });

    test('should add positive and negative numbers correctly', () => {
      expect(add(10, -5)).toBe(5);
      expect(add(-10, 5)).toBe(-5);
    });

    test('should handle zero correctly', () => {
      expect(add(0, 0)).toBe(0);
      expect(add(5, 0)).toBe(5);
      expect(add(0, 5)).toBe(5);
    });

    // Test edge cases
    test('should handle decimal numbers', () => {
      expect(add(1.5, 2.5)).toBe(4);
      expect(add(0.1, 0.2)).toBeCloseTo(0.3);
    });

    test('should handle large numbers', () => {
      expect(add(1000000, 2000000)).toBe(3000000);
      expect(add(Number.MAX_SAFE_INTEGER, 0)).toBe(Number.MAX_SAFE_INTEGER);
    });

    test('should handle negative zero', () => {
      expect(add(-0, 0)).toBe(0);
      expect(add(0, -0)).toBe(0);
    });
  });

  describe('multiply()', () => {
    // Test basic multiplication functionality
    test('should multiply two positive numbers correctly', () => {
      expect(multiply(2, 3)).toBe(6);
      expect(multiply(5, 4)).toBe(20);
    });

    test('should multiply two negative numbers correctly', () => {
      expect(multiply(-2, -3)).toBe(6);
      expect(multiply(-5, -4)).toBe(20);
    });

    test('should multiply positive and negative numbers correctly', () => {
      expect(multiply(5, -3)).toBe(-15);
      expect(multiply(-5, 3)).toBe(-15);
    });

    test('should handle multiplication by zero', () => {
      expect(multiply(0, 0)).toBe(0);
      expect(multiply(5, 0)).toBe(0);
      expect(multiply(0, 5)).toBe(0);
      expect(multiply(-5, 0)).toBe(0);
    });

    test('should handle multiplication by one', () => {
      expect(multiply(1, 1)).toBe(1);
      expect(multiply(5, 1)).toBe(5);
      expect(multiply(1, 5)).toBe(5);
    });

    // Test edge cases
    test('should handle decimal numbers', () => {
      expect(multiply(2.5, 4)).toBe(10);
      expect(multiply(0.5, 0.2)).toBeCloseTo(0.1);
    });

    test('should handle large numbers', () => {
      expect(multiply(1000, 1000)).toBe(1000000);
      expect(multiply(100000, 100000)).toBe(10000000000);
    });

    test('should handle negative zero', () => {
      expect(multiply(-0, 5)).toBe(-0);
      expect(multiply(5, -0)).toBe(-0);
    });
  });

  describe('divide()', () => {
    // Test basic division functionality
    test('should divide two positive numbers correctly', () => {
      expect(divide(6, 2)).toBe(3);
      expect(divide(20, 4)).toBe(5);
    });

    test('should divide two negative numbers correctly', () => {
      expect(divide(-6, -2)).toBe(3);
      expect(divide(-20, -4)).toBe(5);
    });

    test('should divide positive and negative numbers correctly', () => {
      expect(divide(10, -2)).toBe(-5);
      expect(divide(-10, 2)).toBe(-5);
    });

    test('should handle zero as dividend', () => {
      expect(divide(0, 5)).toBe(0);
      expect(divide(0, -5)).toBe(-0);
    });

    test('should handle division by one', () => {
      expect(divide(5, 1)).toBe(5);
      expect(divide(-5, 1)).toBe(-5);
    });

    test('should handle division resulting in decimals', () => {
      expect(divide(5, 2)).toBe(2.5);
      expect(divide(1, 3)).toBeCloseTo(0.333333);
    });

    // Test error handling
    test('should throw error when dividing by zero', () => {
      expect(() => divide(5, 0)).toThrow('Cannot divide by zero');
      expect(() => divide(5, 0)).toThrow(Error);
    });

    test('should throw error when dividing zero by zero', () => {
      expect(() => divide(0, 0)).toThrow('Cannot divide by zero');
    });

    test('should throw error when dividing negative number by zero', () => {
      expect(() => divide(-5, 0)).toThrow('Cannot divide by zero');
    });

    // Test edge cases
    test('should handle large numbers', () => {
      expect(divide(1000000, 1000)).toBe(1000);
      expect(divide(999999, 3)).toBe(333333);
    });

    test('should handle very small numbers', () => {
      expect(divide(0.1, 0.2)).toBeCloseTo(0.5);
      expect(divide(0.001, 0.1)).toBeCloseTo(0.01);
    });

    test('should handle division by negative one', () => {
      expect(divide(5, -1)).toBe(-5);
      expect(divide(-5, -1)).toBe(5);
    });
  });
});
```