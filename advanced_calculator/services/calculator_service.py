from .logger_service import LoggerService
from ..core.engine import CalculatorEngine
from ..core.scientific import ScientificCalculator
from ..storage.history import HistoryStore


class CalculatorService:
    """Coordinates calculation, scientific functions and history."""

    def __init__(self):
        self.engine = CalculatorEngine()
        self.scientific = ScientificCalculator()
        self.history = HistoryStore()
        self.logger = LoggerService()

    def calculate(self, expression):
        result = self.engine.evaluate(expression)
        self.history.add(expression, result)
        self.logger.info(f"Calculated: {expression} = {result}")
        return result

    def scientific_call(self, operation, value, degrees=False):
        func = getattr(self.scientific, operation)
        result = func(value, degrees)
        self.history.add(f"{operation}({value})", result)
        return result
