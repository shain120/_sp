# interpreter.py
from ast_nodes import *

class Interpreter:
    def __init__(self):
        self.env = {}

    
    def run(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.run(stmt)
        elif isinstance(node, VarDecl):
            self.env[node.name] = self.eval(node.expr)
        elif isinstance(node, PrintStmt):
            print(self.eval(node.expr))
        elif isinstance(node, IfStmt):
            if self.eval(node.condition):
                for stmt in node.then_branch:
                    self.run(stmt)
            elif node.else_branch:
                for stmt in node.else_branch:
                    self.run(stmt)
        
        elif isinstance(node, AssignStmt):
            self.env[node.name] = self.eval(node.expr)
        elif isinstance(node, WhileStmt):
            while self.eval(node.condition):
                for stmt in node.body:
                    self.run(stmt)
        else:
            raise Exception(f"Unknown node: {node}")

    def eval(self, expr):
        if isinstance(expr, Number):
            return expr.value
        elif isinstance(expr, String):
            return expr.value
        elif isinstance(expr, VarRef):
            return self.env.get(expr.name, 0)
        elif isinstance(expr, BinOp):
            left = self.eval(expr.left)
            right = self.eval(expr.right)
            if expr.op == "+": return left + right
            if expr.op == "-": return left - right
            if expr.op == "*": return left * right
            if expr.op == "/": return left // right
            if expr.op == ">": return left > right
            if expr.op == "<": return left < right
            if expr.op == "==": return left == right
            if expr.op == "!=": return left != right
        else:
            raise Exception(f"Unknown expression: {expr}")
