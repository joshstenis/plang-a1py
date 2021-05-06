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
    def __init__(self):
        self.yytext = None
        self.curr = None
        self.l_float = re.compile('\d+\.\d+')
        self.comment = re.compile('\/\/.*$')
        self.eof = re.compile('<<EOF>>')

    def rules(self):
        if self.comment.match(self.curr):
            pass
        elif self.curr.isspace():
            pass
        elif self.curr == "\n":
            pass

        elif self.l_float.match(self.curr):
            return Token.L_FLOAT
        elif (_ = self.curr.find("<=")) is not -1:
            return [Token.OP_LEQ, ]
        elif self.curr.find(">=") is not -1:
            return Token.OP_GEQ
        elif self.curr.find("==") is not -1:
            return Token.OP_EQ
        elif self.curr.find("~=") is not -1:
            return Token.OP_DIFF
        elif self.curr.find("++") is not -1:
            return Token.OP_PLUSPLUS
        elif self.curr.find("+=") is not -1:
            return Token.OP_ADDINC
        elif self.curr.find("=") is not -1:
            return Token.OP_ASSIGN
        elif self.curr.find("+") is not -1:
            return Token.OP_ADD
        elif self.curr.find("-") is not -1:
            return Token.OP_SUB
        elif self.curr.find("*") is not -1:
            return Token.OP_MUL
        elif self.curr.find("/") is not -1:
            return Token.OP_DIV
        elif self.curr.find(";") is not -1:
            return ";"
        elif self.curr.find("<") is not -1:
            return Token.OP_LT
        elif self.curr.find(">") is not -1:
            return Token.OP_GT
        elif self.curr.find("integer") is not -1:
            return Token.K_INTEGER
        elif self.curr.find("repeat") is not -1:
            return Token.K_REPEAT
        elif self.curr.find("declare") is not -1:
            return Token.K_DECLARE
        elif self.curr.find("print") is not -1:
            return Token.K_PRINT
        elif self.curr.find("float") is not -1:
            return Token.K_FLOAT
        elif self.curr.find("foreach") is not -1:
            return Token.K_FOREACH
        elif self.curr.find("while") is not -1:
            return Token.K_WHILE
        elif self.curr.find("until") is not -1:
            return Token.K_UNTIL
        elif self.curr.find("begin") is not -1:
            return Token.K_BEGIN
        elif self.curr.find("main") is not -1:
            return Token.K_MAIN
        elif self.curr.find("then") is not -1:
            return Token.K_THEN
        elif self.curr.find("end") is not -1:
            return Token.K_END
        elif self.curr.find("if") is not -1:
            return Token.K_IF
        elif self.curr.isdigit():
            return Token.L_INTEGER
        elif self.curr[0] == "@" and self.curr[1].isalpha():
            return Token.T_ID
        elif self.eof.match(self.curr):
            return Token.T_EOF
        else:
            return self.curr

    # def matchToken(self):
    #     init = self.curr
    #     ret, tok = []
    #     while len(self.curr) > 0:
    #         ret = self.rules()
    #         tok.append(ret[0])
    #         self.curr = self.curr[ret[1]:]
    #     return tok

    def loadWord(self, yyin):
        self.yytext = yyin.split(" ")
        tok = []
        for i in self.yytext:
            self.curr = i
            tok.append(self.rules())
        return tok

def main():
    scnr = Lexer()
    tok = None
    while True:
        tok = scnr.loadWord(input())
        print(tok)

if __name__ == "__main__":
    main()