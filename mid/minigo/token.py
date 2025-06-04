# token.py
KEYWORDS = {"var", "if", "else", "while", "func", "return", "print", "true", "false"}
SYMBOLS = {'(', ')', '{', '}', ';', ',',}

class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value})"

def tokenize(code):
    import re
    tokens = []
    code = code.strip()
    token_spec = [
        ('NUMBER',  r'\d+'),
        ('ID',      r'[a-zA-Z_]\w*'),
        ('OP',      r'(==|!=|<=|>=|[+\-*/=<>])'),  # = 是 OP
        ('SKIP',    r'[ \t]+'),
        ('NEWLINE', r'\n'),
        ('SYMBOL',  r'[{}();,]'),  # = 不在這裡
        ('STRING',  r'"[^"]*"'),
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_spec)
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            tokens.append(Token('NUMBER', int(value)))
        elif kind == 'ID':
            tokens.append(Token('KEYWORD' if value in KEYWORDS else 'ID', value))
        elif kind == 'OP':
            tokens.append(Token('OP', value))
        elif kind == 'STRING':
            tokens.append(Token('STRING', value.strip('"')))
        elif kind == 'SYMBOL':
            tokens.append(Token('SYMBOL', value))


    return tokens
