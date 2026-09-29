import math


class EquationSolver:
    """Solves linear and quadratic equations."""

    @staticmethod
    def linear(a, b):
        if a == 0:
            if b == 0:
                return "Infinitely many solutions"
            return "No solution"
        return [-b / a]

    @staticmethod
    def quadratic(a, b, c):
        if a == 0:
            return EquationSolver.linear(b, c)

        discriminant = b * b - 4 * a * c
        if discriminant > 0:
            root = math.sqrt(discriminant)
            return [(-b + root) / (2 * a), (-b - root) / (2 * a)]
        if discriminant == 0:
            return [-b / (2 * a)]

        root = math.sqrt(-discriminant)
        real = -b / (2 * a)
        imag = root / abs(2 * a)
        return [complex(real, imag), complex(real, -imag)]
