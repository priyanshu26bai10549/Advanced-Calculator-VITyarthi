class CalculatorError(Exception):
    """Base exception for calculator errors."""


class InvalidExpressionError(CalculatorError):
    """Raised when an expression is invalid or unsafe."""


class CalculationError(CalculatorError):
    """Raised when a mathematical operation cannot be completed."""
