from array_stack import *

class FullyParenthesisedExpression():
    def __init__(self, expression):
        self.expression = expression
        self.token = []
        self.get_token()
        self.stack = ArrayStack()

    def get_token(self):
        number_string = ""
        for c in self.expression:
            if c == ' ':
                continue
            if c.isdigit():
                number_string += c
                continue
            else:
                if number_string:
                    self.token.append(int(number_string))
                    number_string = ""
                self.token.append(c)

    def evaluate(self):
        for c in self.token:
            if type(c) == int:
                self.stack.push(c)
                continue
            if c in "{[(":
                continue
            elif c in ")}]":
                number_right = self.stack.pop()
                operator = self.stack.pop()
                number_left = self.stack.pop()
                if operator == "+":
                    self.stack.push(number_left + number_right)
                if operator == "-":
                    self.stack.push(number_left - number_right)
                if operator == "*":
                    self.stack.push(number_left * number_right)
                if operator == "/":
                    self.stack.push(number_left / number_right)
            else:
                self.stack.push(c)
        print(self.stack.peek())





expression = FullyParenthesisedExpression("(12 + [{[13 + (4 + 5)] - 10} / (7 * 8)])")
expression.evaluate()