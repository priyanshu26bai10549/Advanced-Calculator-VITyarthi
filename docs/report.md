# Advanced Calculator — Project Report

## 1. Cover Page
**Project Title:** Advanced Calculator  
**Course:** Python Essentials 
**Student Name:** Priyanshu Mewada  
**Registration Number:** 26BAI10549 
**Faculty:** Dr. Lakshmi D 
**Academic Year:** 2026

## 2. Introduction
The Advanced Calculator is a Python application designed to provide a collection of mathematical operations through a modular architecture. It extends basic arithmetic with scientific calculations, equation solving, statistics, matrix operations and history management.

## 3. Problem Statement
A calculator project can become more meaningful when it goes beyond four-function arithmetic and demonstrates validation, modular design, data processing, persistence, testing and error handling.

## 4. Objectives
- Build an original calculator application.
- Apply Python programming concepts in a real-world utility.
- Separate responsibilities into reusable modules.
- Provide multiple mathematical capabilities.
- Demonstrate validation and error handling.
- Maintain calculation history.
- Test important mathematical operations.

## 5. Functional Requirements
1. Basic expression calculation.
2. Scientific calculations.
3. Factorial and percentage.
4. Equation solving.
5. Statistics.
6. Matrix operations.
7. History viewing and clearing.
8. Logging and error reporting.

## 6. Non-Functional Requirements
- Performance
- Usability
- Reliability
- Maintainability
- Resource efficiency
- Security
- Error handling
- Logging/monitoring

## 7. System Architecture
See `architecture.md`.

## 8. Design Diagrams
See:
- `use_case.md`
- `workflow.md`
- `sequence_diagram.md`
- `class_diagram.md`
- `er_diagram.md`

## 9. Design Decisions & Rationale
Python's standard library was selected to keep installation simple and demonstrate core programming concepts. The application uses a modular architecture so calculation logic, validation, services and storage are separated.

A restricted AST-based expression evaluator was selected instead of unrestricted `eval()` for safer expression processing.

JSON was selected for lightweight history persistence because the project does not require relational database functionality.

## 10. Implementation Details
The core package contains:
- Expression validation
- Arithmetic evaluation
- Scientific functions
- Equation solver
- Statistics calculator
- Matrix calculator
- Exception classes

The service package coordinates calculations and logging. The storage package manages calculation history.

## 11. Screenshots / Results
Screenshots after running the application:
1. Main menu:<img width="1432" height="390" alt="image" src="https://github.com/user-attachments/assets/c23a4555-fe92-4f87-9dc2-3eb24f8f6102" />
2. Basic calculation:<img width="762" height="342" alt="image" src="https://github.com/user-attachments/assets/a6d4f30e-ee1c-4ad8-815a-91f78bb48d35" />
3. Scientific calculation:<img width="513" height="397" alt="image" src="https://github.com/user-attachments/assets/bbcda662-1a1a-4733-b572-faafa01171dc" />
4. Equation solving: <img width="341" height="401" alt="image" src="https://github.com/user-attachments/assets/bbba4825-04ce-46f5-97c9-a6501959a672" />
5. Statistics:<img width="767" height="482" alt="image" src="https://github.com/user-attachments/assets/fd3c50e0-8c10-4607-8ce9-ac063390cdc1" />
6. History:<img width="722" height="435" alt="image" src="https://github.com/user-attachments/assets/dcd8d400-9359-4402-b01f-75a54e89937e" />


## 12. Testing Approach
Unit tests are provided using Python's `unittest` framework. Tests cover arithmetic, powers, invalid division, factorial, percentage, square root, logarithm and quadratic roots.

Run:
```bash
python -m unittest discover -s tests -v
```
Screenshot:<img width="851" height="307" alt="Screenshot 2026-09-29 212205" src="https://github.com/user-attachments/assets/e819623f-08f4-4076-81d7-6b3725b19a49" />


## 13. Challenges Faced
- Designing a restricted mathematical expression evaluator.
- Handling invalid mathematical domains.
- Keeping modules independent.
- Managing persistent calculation history.
- Testing multiple mathematical cases.

## 14. Learnings & Key Takeaways
- Modular Python architecture
- Object-oriented design
- Input validation
- Exception handling
- File-based persistence
- Unit testing
- Logging
- Git/GitHub project organization

## 15. Future Enhancements
- Graph plotting
- GUI using Tkinter/PySide
- More matrix operations
- Symbolic algebra
- Unit conversion
- Export history to CSV
- User profiles
- More automated test coverage

## 16. References
- Python standard library documentation
- Course/VITyarthi project instructions supplied for this project
