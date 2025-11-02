from dataclasses import dataclass
from typing import List
import math

class Token:
    """Represents a pair of two teeth, (a,b) in integers; first one 2-3 digits second one 1 digit"""
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"Token(a={self.a}, b={self.b}"



class Interpreter:


    def __init__(self):
        self.stack = []
        self.program = []
        self.ip = 0
        self.running = False
        self.stringmode = False

    
    def lex(self, teeth: List[float]) -> List[Token]:
        """
        Convert a flat list of integers into a list of Token objects,
        each representing a pair of adjacent integers.
        """
        if len(teeth) % 2 != 0:
            raise SyntaxError("Number of integers must be even to form pairs")

        self.tokens = [
            Token(math.floor(100*teeth[i]), math.floor(10*teeth[i + 1]))
            for i in range(0, len(teeth), 2) 
        ]

        return self.tokens


    def load_program(self, code: str):

        self.program = self.lex(code)
        self.ip = 0


    def run(self):

        self.running = True
        while self.running and 0 <= self.ip < len(self.program):
            token = self.program[self.ip]
            self.execute(token)
            self.ip += 1

    def execute(self, token: Token):
        op = token.b
        # PUSH
        if op == 0:
            self.stack.append(token.a)

        # ADD
        elif op == -6:
            if len(self.stack) >= 2:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)

        # SUB
        elif op == -5:
            if len(self.stack) >= 2:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)

        # MUL
        elif op == -4:
            if len(self.stack) >= 2:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)

        # DIV
        elif op == -3:
            if len(self.stack) >= 2:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a // b if b != 0 else 0)
        
        #ENTER DATA ENTRY MODE
        elif op == -1:


        # PRINT_NUM
        elif op == 0:
            if self.stack:
                print(int(self.stack[-1]))

        # PRINT_CHAR
        elif op == 1:
            if self.stack:
                val = int(self.stack[-1]) % 256
                print(chr(val), end='')

        # JMP
        elif op == 2:
            self.ip = token.a - 1

        # JZ
        elif op == 3:
            if self.stack and self.stack[-1] == 0:
                self.ip = token.a - 1


        #PRINT_STACK
        elif op == 4:
            print(self.stack)

        #PRINT_CHARS
        elif op == 5:

            chars = [
                chr(val) if 0 <= val <= 127 else '?'
                for val in self.stack
            ]
            print("".join(chars))

        # HALT
        elif op == 6:
            self.running = False

        # HALT BUT FUNNY
        elif op >= 7 or op <= -6:
            print(".....Waow.....(your teeth are really fucked up)")
            self.running = False
        else:
            raise ValueError(f"Unknown opcode: {op}")
        

code = [.72,.0,.0,.6,1.01,.0,.0,.6,1.08,.0,.0,.6,1.08,.0,.0,.6,1.11,.0,.0,.6,.32,.0,.0,.6,1.19,.0,.0,.6,1.11,.0,.0,.6,1.15,.0,.0,.6,1.08,.0,.0,.6,1.00,0,0,.6,0,.9]
code2 = [.72, 0, .72, 0, .72, 0, .72, 0, .72, 0, 0, .9]

interp = Interpreter()
interp.load_program(code2)
interp.run()