# main.py
from token import tokenize
from parser import Parser
from interpreter import Interpreter

with open("examples/demo1.mgo") as f:
    code = f.read()

tokens = tokenize(code)
parser = Parser(tokens)
tree = parser.parse()
interpreter = Interpreter()
interpreter.run(tree)
