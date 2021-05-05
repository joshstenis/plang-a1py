import io, re, sys
from enum import Enum

class Token(Enum):
    K_FOREACH = 200
    K_PRINT = 201
    K_WHILE = 202
    K_REPEAT = 203
    K_UNTIL = 204
    K_BEGIN = 205
    K_END = 206
    K_DECLARE = 209
    K_IF = 210
    K_THEN = 211
    K_MAIN = 212
    K_INTEGER = 213
    K_FLOAT = 214
    OP_ASSIGN = 220
    OP_ADD = 221
    OP_SUB = 222
    OP_MUL = 223
    OP_DIV = 224
    OP_LT = 225
    OP_GT = 226
    OP_LEQ = 227
    OP_GEQ = 228
    OP_EQ  = 229
    # OP_DIFF is ~=
    OP_DIFF = 230
    # OP_PLUSPLUS is ++
    OP_PLUSPLUS = 231
    # OP_ADDINC is +=
    OP_ADDINC = 232
    CAR_A = 400
    CAR_B = 401
    CAR_C = 402
    CAR_AB = 403
    # literals
    T_ID = 240
    L_INTEGER = 241
    L_FLOAT = 242
    T_EOF = 280

class Lexer(object):
    def __init__(self, stream):
        self.stream = stream
        self.curr = None
        self.modifier = 0
        self.l_float = re.compile('\d+(\.\d+)?')
        self.comment = re.compile('\/\/.*$')
        self.eof = re.compile('<<EOF>>')

    def nextToken(self):
        if self.curr is None:
            return None

        if comment.match(self.curr):
            pass
        elif self.curr.isspace():
            pass
        elif self.curr == "\n":
            pass
        elif self.l_float.match(self.curr):
            return L_FLOAT
        elif self.curr == "=":
            return OP_ASSIGN
        elif self.curr == "+":
            return OP_ADD
        elif self.curr == "-":
            return OP_SUB
        elif self.curr == "*":
            return OP_MUL
        elif self.curr == "/":
            return OP_DIV
        elif self.curr == ";":
            return ";"
        elif self.curr == "<":
            return OP_LT
        elif self.curr == ">":
            return OP_GT
        elif self.curr == "<=":
            return OP_LEQ
        elif self.curr == ">=":
            return OP_GEQ
        elif self.curr == "==":
            return OP_EQ
        elif self.curr == "~=":
            return OP_DIFF
        elif self.curr == "++":
            return OP_PLUSPLUS
        elif self.curr == "+=":
            return OP_ADDINC
        elif self.curr.isdigit():
            return L_INTEGER
        elif self.curr == "main":
            return K_MAIN
        elif self.curr == "integer":
            return K_INTEGER
        elif self.curr == "float":
            return K_FLOAT
        elif self.curr == "foreach":
            return K_FOREACH
        elif self.curr == "begin":
            return K_BEGIN
        elif self.curr == "end":
            return K_END
        elif self.curr == "repeat":
            return K_REPEAT
        elif self.curr == "until":
            return K_UNTIL
        elif self.curr == "then":
            return K_THEN
        elif self.curr == "while":
            return K_WHILE
        elif self.curr == "declare":
            return K_DECLARE
        elif self.curr == "if":
            return K_IF
        elif self.curr == "print":
            return K_PRINT
        elif eof.match(self.curr):
            return T_EOF
        elif self.curr.isalpha():
            return T_ID

    def getWord(self):
        if self.modifier >= len(stream):
            return None

def main(argv):
    prgm = argv[0]

    scnr = Lexer(prgm)
    tok = scnr.nextToken()
    while tok is not None:
        print(tok)
        tok = scnr.nextToken()

if __name__ == "__main__":
    main(sys.argv[1:])