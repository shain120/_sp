# ast_nodes.py
class Program:
    def __init__(self, statements):
        self.statements = statements

class VarDecl:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class PrintStmt:
    def __init__(self, expr):
        self.expr = expr

class IfStmt:
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Number:
    def __init__(self, value):
        self.value = value

class String:
    def __init__(self, value):
        self.value = value

class VarRef:
    def __init__(self, name):
        self.name = name

class WhileStmt:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body


class AssignStmt:
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
