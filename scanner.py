import io, re
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
        self.l_float = re.compile('\d+(\.\d+)?')

    def nextToken(self):
        if self.curr is None:
            return None

        if self.l_float.match(self.curr):
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

    def skipWhitespace(self):
        # Skips whitespace in stream

def main():
    # Print each token in while loop

if __name__ == "__main__":
    main()