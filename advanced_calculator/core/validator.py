import ast
import operator
import re

from .exceptions import InvalidExpressionError


class ExpressionValidator:
    """Validates expressions before evaluation.

    The evaluator intentionally accepts only a small mathematical grammar.
    """

    ALLOWED_BINOPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.FloorDiv: operator.floordiv,
    }
    ALLOWED_UNARYOPS = {ast.UAdd: operator.pos, ast.USub: operator.neg}

    def validate(self, expression: str) -> ast.Expression:
        if not expression or not expression.strip():
            raise InvalidExpressionError("Expression cannot be empty.")

        if len(expression) > 250:
            raise InvalidExpressionError("Expression is too long.")

        if re.search(r"__|import|exec|eval|open|globals|locals", expression, re.I):
            raise InvalidExpressionError("Unsafe expression detected.")

        try:
            tree = ast.parse(expression, mode="eval")
        except SyntaxError as exc:
            raise InvalidExpressionError("Invalid mathematical expression.") from exc

        self._validate_node(tree.body)
        return tree

    def _validate_node(self, node):
        if isinstance(node, ast.Constant):
            if not isinstance(node.value, (int, float)) or isinstance(node.value, bool):
                raise InvalidExpressionError("Only numeric constants are allowed.")
            return

        if isinstance(node, ast.BinOp):
            if type(node.op) not in self.ALLOWED_BINOPS:
                raise InvalidExpressionError("Operator is not supported.")
            self._validate_node(node.left)
            self._validate_node(node.right)
            return

        if isinstance(node, ast.UnaryOp):
            if type(node.op) not in self.ALLOWED_UNARYOPS:
                raise InvalidExpressionError("Unary operator is not supported.")
            self._validate_node(node.operand)
            return

        raise InvalidExpressionError("Only arithmetic expressions are allowed.")
