# parser.py
from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, expected_type=None, expected_value=None):
        token = self.peek()
        if token is None:
            raise Exception("Unexpected end of input")
        if expected_type and token.type != expected_type:
            raise Exception(f"Expected type {expected_type}, got {token.type}")
        if expected_value and token.value != expected_value:
            raise Exception(f"Expected value {expected_value}, got {token.value}")
        self.pos += 1
        return token

    def parse(self):
        statements = []
        while self.peek():
            statements.append(self.statement())
        return Program(statements)

    
    
    def statement(self):
        token = self.peek()
        if token.type == "KEYWORD":
            if token.value == "var":
                return self.var_decl()
            elif token.value == "print":
                return self.print_stmt()
            elif token.value == "if":
                return self.if_stmt()
            elif token.value == "while":
                return self.while_stmt()
        elif token.type == "ID":
            # 支援簡單賦值語句 like: i = i + 1
            name = self.eat("ID").value
            self.eat("OP", "=")
            expr = self.expression()
            return AssignStmt(name, expr)
        raise Exception("Unknown statement")



    def var_decl(self):
        self.eat("KEYWORD", "var")
        name = self.eat("ID").value
        self.eat("OP", "=")
        expr = self.expression()
        return VarDecl(name, expr)

    def print_stmt(self):
        self.eat("KEYWORD", "print")
        self.eat("SYMBOL", "(")
        expr = self.expression()
        self.eat("SYMBOL", ")")
        return PrintStmt(expr)

    def if_stmt(self):
        self.eat("KEYWORD", "if")
        self.eat("SYMBOL", "(")
        condition = self.expression()
        self.eat("SYMBOL", ")")
        self.eat("SYMBOL", "{")
        then_branch = []
        while self.peek().value != "}":
            then_branch.append(self.statement())
        self.eat("SYMBOL", "}")
        else_branch = None
        if self.peek() and self.peek().value == "else":
            self.eat("KEYWORD", "else")
            self.eat("SYMBOL", "{")
            else_branch = []
            while self.peek().value != "}":
                else_branch.append(self.statement())
            self.eat("SYMBOL", "}")
        return IfStmt(condition, then_branch, else_branch)

    def expression(self):
        left = self.term()
        while self.peek() and self.peek().type == "OP":
            op = self.eat("OP").value
            right = self.term()
            left = BinOp(left, op, right)
        return left

    def term(self):
        token = self.eat()
        if token.type == "NUMBER":
            return Number(token.value)
        elif token.type == "STRING":
            return String(token.value)
        elif token.type == "ID":
            return VarRef(token.value)

    def while_stmt(self):
        self.eat("KEYWORD", "while")
        self.eat("SYMBOL", "(")
        condition = self.expression()
        self.eat("SYMBOL", ")")
        self.eat("SYMBOL", "{")
        body = []
        while self.peek().value != "}":
            body.append(self.statement())
        self.eat("SYMBOL", "}")
        return WhileStmt(condition, body)
