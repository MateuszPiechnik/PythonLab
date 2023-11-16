class Complex:
    def __init__(self, re, im=0.0):
        self.re = re
        self.im = im

    def __add__(self, other):
        return self.re + other.re, self.im + other.im

    def __sub__(self, other):
        return self.re - other.re, self.im - other.im


number1 = Complex(5, 2j)
number2 = Complex(10, 4j)

print(number2 + number1)
print(number1 - number2)