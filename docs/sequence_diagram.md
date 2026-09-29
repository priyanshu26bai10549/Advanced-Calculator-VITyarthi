# Sequence Diagram

```text
User -> App: Select calculation
App -> CalculatorService: calculate(expression)
CalculatorService -> CalculatorEngine: evaluate(expression)
CalculatorEngine -> ExpressionValidator: validate(expression)
ExpressionValidator --> CalculatorEngine: validated AST
CalculatorEngine --> CalculatorService: result
CalculatorService -> HistoryStore: add(expression,result)
CalculatorService -> LoggerService: info(...)
CalculatorService --> App: result
App --> User: Display result
```
