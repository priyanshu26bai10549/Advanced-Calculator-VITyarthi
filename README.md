# Advanced Calculator

## VITyarthi — Build Your Own Project

A modular Python-based Advanced Calculator designed according to the VITyarthi project requirements.

## 1. Overview
The project combines basic arithmetic, scientific mathematics, equation solving, statistics, matrix operations, history management, validation and logging in one application.

## 2. Major Functional Modules
### Module 1 — Basic & Scientific Calculation
- Arithmetic expressions
- Powers and modulo
- Trigonometric functions
- Logarithms
- Square roots
- Factorial and percentage

### Module 2 — Advanced Mathematical Operations
- Quadratic equation solving
- Statistics
- Matrix addition
- Matrix multiplication

### Module 3 — History & Application Services
- Calculation history
- Persistent JSON storage
- Logging
- Validation and error handling

## 3. Non-Functional Requirements
- **Performance:** normal calculations should complete immediately for supported input limits.
- **Usability:** menu-driven interaction and clear error messages.
- **Reliability:** invalid input and mathematical domain errors are handled.
- **Maintainability:** functionality is separated into reusable modules/classes.
- **Resource efficiency:** standard-library implementation with bounded expression/history sizes.
- **Security:** expressions are parsed through a restricted AST validator rather than unrestricted Python evaluation.

## 4. Technologies
- Python 3.10+
- Python standard library
- unittest
- JSON
- Git/GitHub

## 5. Project Structure
```text
AdvancedCalculator_VITyarthi/
├── advanced_calculator/
│   ├── core/
│   │   ├── engine.py
│   │   ├── equation.py
│   │   ├── exceptions.py
│   │   ├── matrix.py
│   │   ├── scientific.py
│   │   ├── statistics.py
│   │   └── validator.py
│   ├── services/
│   │   ├── calculator_service.py
│   │   └── logger_service.py
│   ├── storage/
│   │   └── history.py
│   └── app.py
├── tests/
│   └── test_calculator.py
├── data/
├── docs/
├── main.py
├── requirements.txt
├── statement.md
├── README.md
└── .gitignore
```

## 6. Installation
```bash
git clone <your-github-repository-url>
cd AdvancedCalculator_VITyarthi
python -m venv .venv
```

Activate the virtual environment, then run:
```bash
python main.py
```

No third-party packages are required.

## 7. Testing
Run:
```bash
python -m unittest discover -s tests -v
```

## 8. Example
```text
Choose an option: 1
Expression: 12*(5+3)
Result: 96
```

## 9. Version Control
Recommended Git workflow:
```bash
git init
git add .
git commit -m "Initial Advanced Calculator project"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```

## 10. Academic Note
This project is structured to address the VITyarthi requirements for functional modules, non-functional requirements, modular implementation, validation/error handling, testing, documentation, GitHub repository contents and project-report artefacts.
