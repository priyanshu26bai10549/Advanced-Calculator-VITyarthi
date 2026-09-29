import ast
import math
import operator

from .exceptions import CalculationError
from .validator import ExpressionValidator


class CalculatorEngine:
    """Safe arithmetic engine for basic and scientific calculations."""

    def __init__(self):
        self.validator = ExpressionValidator()

    def evaluate(self, expression: str) -> float:
        tree = self.validator.validate(expression)
        try:
            result = self._evaluate_node(tree.body)
        except ZeroDivisionError as exc:
            raise CalculationError("Division by zero is not allowed.") from exc
        except (OverflowError, ValueError) as exc:
            raise CalculationError(str(exc)) from exc

        if not math.isfinite(float(result)):
            raise CalculationError("Result is outside the supported numeric range.")
        return result

    def _evaluate_node(self, node):
        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.UnaryOp):
            return ExpressionValidator.ALLOWED_UNARYOPS[type(node.op)](
                self._evaluate_node(node.operand)
            )

        if isinstance(node, ast.BinOp):
            left = self._evaluate_node(node.left)
            right = self._evaluate_node(node.right)

            if type(node.op) is ast.Pow and abs(right) > 100:
                raise CalculationError("Exponent is limited to 100.")
            if abs(left) > 1e100 or abs(right) > 1e100:
                raise CalculationError("Input magnitude is too large.")

            return ExpressionValidator.ALLOWED_BINOPS[type(node.op)](left, right)

        raise CalculationError("Unsupported expression node.")

    @staticmethod
    def factorial(n: int) -> int:
        if n < 0 or int(n) != n:
            raise CalculationError("Factorial requires a non-negative integer.")
        if n > 1000:
            raise CalculationError("Factorial input is limited to 1000.")
        return math.factorial(int(n))

    @staticmethod
    def percentage(value: float, percent: float) -> float:
        return value * percent / 100

    @staticmethod
    def power(base: float, exponent: float) -> float:
        if abs(exponent) > 100:
            raise CalculationError("Exponent is limited to 100.")
        return math.pow(base, exponent)
