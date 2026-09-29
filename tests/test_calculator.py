import unittest

from advanced_calculator.core.engine import CalculatorEngine
from advanced_calculator.core.equation import EquationSolver
from advanced_calculator.core.scientific import ScientificCalculator


class TestCalculatorEngine(unittest.TestCase):
    def setUp(self):
        self.engine = CalculatorEngine()

    def test_basic_expression(self):
        self.assertEqual(self.engine.evaluate("2 + 3 * 4"), 14)

    def test_power(self):
        self.assertEqual(self.engine.evaluate("2 ** 5"), 32)

    def test_division_by_zero(self):
        with self.assertRaises(Exception):
            self.engine.evaluate("10 / 0")

    def test_factorial(self):
        self.assertEqual(self.engine.factorial(5), 120)

    def test_percentage(self):
        self.assertEqual(self.engine.percentage(200, 10), 20)


class TestScientific(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(ScientificCalculator.sqrt(81), 9)

    def test_log(self):
        self.assertAlmostEqual(ScientificCalculator.log(100), 2)


class TestEquation(unittest.TestCase):
    def test_quadratic(self):
        roots = EquationSolver.quadratic(1, -3, 2)
        self.assertIn(1.0, roots)
        self.assertIn(2.0, roots)


if __name__ == "__main__":
    unittest.main()
