import codewars_test as test
from solution import Calculator

@test.describe("Fixed Tests")
def fixed_tests():
    test.assert_equals(Calculator().evaluate("2 / 2 + 3 * 4 - 6"), 7)
    test.assert_equals(Calculator().evaluate("3 * 4 + 3 * 7 - 6"), 27)
    test.assert_equals(Calculator().evaluate('1 + 1'), 2)
    test.assert_equals(Calculator().evaluate("( ( ( ( 1 ) * 2 ) ) )"), 2)
    test.assert_equals(Calculator().evaluate("( ( ( ( ( ( ( 5 ) ) ) ) ) ) )"), 5)
    test.assert_equals(Calculator().evaluate("2 * ( 2 * ( 2 * ( 2 * 1 ) ) )"), 16)
    test.assert_equals(Calculator().evaluate("3 * ( 4 + 7 ) - 6"), 27)
    test.expect(type(Calculator().evaluate('1 + 1')) in [float, int], "Your result's type should be either int or float")
    
test.it("Tests")
for key, val in {
  "127": 127,
  "2 + 3": 5,
  "2 - 3 - 4": -5,
  "10 * 5 / 2": 25,
  "2 / 2 + 3 * 4 - 6": 7,
  "2 + 3 * 4 / 3 - 6 / 3 * 3 + 8": 8,
  "1.1 + 2.2 + 3.3": 6.6,
  "1.1 * 2.2 * 3.3": 7.986
}.items():
    actual = Calculator().evaluate(key)
    test.expect(isinstance(actual, (float, int)), "Your result should be a number, not: "+str(type(actual)))
    test.expect(abs(actual-val) < 1e-12, "Expected %s == %s, but got %s" % (key, val, actual))