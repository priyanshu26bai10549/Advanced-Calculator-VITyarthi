from .services.calculator_service import CalculatorService
from .core.equation import EquationSolver
from .core.statistics import StatisticsCalculator
from .core.matrix import MatrixCalculator


def show_menu():
    print("\n=== ADVANCED CALCULATOR ===")
    print("1. Basic expression")
    print("2. Scientific function")
    print("3. Factorial")
    print("4. Percentage")
    print("5. Solve quadratic equation")
    print("6. Statistics")
    print("7. Matrix addition")
    print("8. Matrix multiplication")
    print("9. View history")
    print("10. Clear history")
    print("0. Exit")


def main():
    service = CalculatorService()

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        try:
            if choice == "0":
                print("Thank you for using Advanced Calculator.")
                break

            if choice == "1":
                expression = input("Expression (e.g. 12*(5+3)): ")
                print("Result:", service.calculate(expression))

            elif choice == "2":
                op = input("Function (sin/cos/tan/log/ln/sqrt): ").strip().lower()
                value = float(input("Value: "))
                degrees = input("Use degrees? (y/n): ").strip().lower() == "y"
                if op in {"log", "ln", "sqrt"}:
                    degrees = False
                print("Result:", service.scientific_call(op, value, degrees))

            elif choice == "3":
                n = int(input("Non-negative integer: "))
                print("Result:", service.engine.factorial(n))

            elif choice == "4":
                value = float(input("Value: "))
                percent = float(input("Percentage: "))
                print("Result:", service.engine.percentage(value, percent))

            elif choice == "5":
                a = float(input("a: "))
                b = float(input("b: "))
                c = float(input("c: "))
                print("Roots:", EquationSolver.quadratic(a, b, c))

            elif choice == "6":
                raw = input("Enter comma-separated numbers: ")
                values = StatisticsCalculator.parse(raw)
                for key, value in StatisticsCalculator.summary(values).items():
                    print(f"{key}: {value}")

            elif choice in {"7", "8"}:
                print("Use Python list syntax, e.g. [[1,2],[3,4]]")
                a = eval(input("Matrix A: "), {"__builtins__": {}}, {})
                b = eval(input("Matrix B: "), {"__builtins__": {}}, {})
                if choice == "7":
                    print(MatrixCalculator.add(a, b))
                else:
                    print(MatrixCalculator.multiply(a, b))

            elif choice == "9":
                for item in service.history.all():
                    print(item["timestamp"], "|", item["expression"], "=", item["result"])

            elif choice == "10":
                service.history.clear()
                print("History cleared.")

            else:
                print("Invalid option.")

        except Exception as exc:
            service.logger.error(str(exc))
            print("Error:", exc)


if __name__ == "__main__":
    main()
