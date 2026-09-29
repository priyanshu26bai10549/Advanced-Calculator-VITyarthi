class MatrixCalculator:
    """Small matrix utility supporting addition and multiplication."""

    @staticmethod
    def validate(matrix):
        if not matrix or not all(isinstance(row, list) and row for row in matrix):
            raise ValueError("Matrix cannot be empty.")
        width = len(matrix[0])
        if any(len(row) != width for row in matrix):
            raise ValueError("All matrix rows must have the same length.")
        return matrix

    @classmethod
    def add(cls, a, b):
        cls.validate(a)
        cls.validate(b)
        if len(a) != len(b) or len(a[0]) != len(b[0]):
            raise ValueError("Matrices must have the same dimensions.")
        return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
                for i in range(len(a))]

    @classmethod
    def multiply(cls, a, b):
        cls.validate(a)
        cls.validate(b)
        if len(a[0]) != len(b):
            raise ValueError("Columns of A must equal rows of B.")
        return [
            [sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))]
            for i in range(len(a))
        ]
