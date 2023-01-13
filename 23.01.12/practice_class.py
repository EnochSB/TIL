class Calculator():
    def __init__(self, number1: int, number2: int):
        self.number1 = number1
        self.number2 = number2
    
    def plus(self):
        return self.number1 + self.number2
    
    def minus(self):
        return self.number1 - self.number2
    
    def multiply(self):
        return self.number1 * self.number2
    
    def division(self):
        return self.number1 // self.number2
    
    def print(self):
        print(f'number1 = {self.number1}, number2 = {self.number2}')
        print(f'합 : {self.plus()}')
        print(f'빼기 : {self.minus()}')
        print(f'곱 : {self.multiply()}')
        return f'몫 : {self.division()}'

calculator = Calculator(-2, 2)
print(calculator.print())