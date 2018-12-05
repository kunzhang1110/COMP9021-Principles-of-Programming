# Use stack to evaluate expressions

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def peek(self):
        if self.is_empty():
            raise Exception('Empty stack')
        return self._data[-1]

    def push(self, datum):
        self._data.append(datum)

    def pop(self):
        if self.is_empty():
            raise Exception('Empty stack')
        return self._data.pop()


class FullyParenthesisedExpression():
    def __init__(self, input_string):
        self.expression = input_string
        self.get_token()
        self.Stack = ArrayStack()

    def get_token(self):
        self.token = []
        number_flag = 0
        number_string = ""
        for i in self.expression:
            if i == ' ':
                continue
            if i.isdigit():
                number_flag = 1
                number_string += i
                continue
            else:
                if number_flag == 1:
                    self.token.append(int(number_string))
                    number_flag = 0
                    number_string = ""
                self.token.append(i)
        if number_flag == 1:
            self.token.append(int(number_string))
        print(self.token)

    def evaluate(self):
        for i in self.token:
            if type(i) == str:
                if i in "{([":
                    continue
                elif i in "}])":
                    num_2 = self.Stack.pop()
                    operator = self.Stack.pop()
                    num_1 = self.Stack.pop()
                    if operator == '+':
                        self.Stack.push(num_1 + num_2)
                    if operator == '-':
                        self.Stack.push(num_1 - num_2)
                    if operator == '*':
                        self.Stack.push(num_1 * num_2)
                    if operator == '/':
                        self.Stack.push(num_1 / num_2)
                    continue
                else:
                    self.Stack.push(i)
            else:
                self.Stack.push(i)
        return self.Stack.peek()

if __name__ == '__main__':
    print('Testing 2:')
    fully_parenthesised_expression = FullyParenthesisedExpression('2')
    print(fully_parenthesised_expression.evaluate())
    print('Testing (2 + 3):')
    fully_parenthesised_expression = FullyParenthesisedExpression('(2 + 3)')
    print(fully_parenthesised_expression.evaluate())
    print('Testing [(2 + 3) / 10]:')
    fully_parenthesised_expression = FullyParenthesisedExpression('[(2 + 3) / 10]')
    print(fully_parenthesised_expression.evaluate())
    print('Testing (12 + [{[13 + (4 + 5)] - 10} / (7 * 8)]):')
    fully_parenthesised_expression = FullyParenthesisedExpression('(12 + [{[13 + (4 + 5)] - 10} / (7 * 8)])')
    print(fully_parenthesised_expression.evaluate())
