import operator
import re

class CalculationHandler:
    def __init__(self):
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

    def calculate(self, expression):
        # Split the expression into numbers and operators
        numbers = re.findall(r'\d+', expression)
        ops = re.findall(r'[+*/-]', expression)

        # Convert the numbers to integers
        numbers = list(map(int, numbers))

        # Perform the calculations
        result = numbers[0]
        for i in range(1, len(numbers)):
            result = self.operators[ops[i-1]](result, numbers[i])

        return str(result)

if __name__ == "__main__":
    handler = CalculationHandler()
    while True:
        expression = input("Enter your expression: ")
        result = handler.calculate(expression)
        print("Result: ", result)
