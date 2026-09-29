import math

from .exceptions import CalculationError


class ScientificCalculator:
    """Scientific operations with domain validation."""

    @staticmethod
    def sin(value: float, degrees: bool = False) -> float:
        return math.sin(math.radians(value) if degrees else value)

    @staticmethod
    def cos(value: float, degrees: bool = False) -> float:
        return math.cos(math.radians(value) if degrees else value)

    @staticmethod
    def tan(value: float, degrees: bool = False) -> float:
        angle = math.radians(value) if degrees else value
        if abs(math.cos(angle)) < 1e-12:
            raise CalculationError("Tangent is undefined at this angle.")
        return math.tan(angle)

    @staticmethod
    def log(value: float, base: float = 10) -> float:
        if value <= 0 or base <= 0 or base == 1:
            raise CalculationError("Invalid logarithm domain or base.")
        return math.log(value, base)

    @staticmethod
    def ln(value: float) -> float:
        if value <= 0:
            raise CalculationError("Natural logarithm requires a positive value.")
        return math.log(value)

    @staticmethod
    def sqrt(value: float) -> float:
        if value < 0:
            raise CalculationError("Square root requires a non-negative value.")
        return math.sqrt(value)
