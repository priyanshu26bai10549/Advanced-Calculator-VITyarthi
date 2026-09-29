# Class Diagram

```text
CalculatorService
  |
  +--> CalculatorEngine
  |      +--> ExpressionValidator
  |
  +--> ScientificCalculator
  +--> HistoryStore
  +--> LoggerService

EquationSolver
StatisticsCalculator
MatrixCalculator

Exceptions:
  CalculatorError
      +--> InvalidExpressionError
      +--> CalculationError
```
