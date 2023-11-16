class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.a = 0
        self.b = 1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter >=self.steps:
            raise StopIteration
        self.b += self.a
        self.a = self.b - self.a
        self.counter +=1
        return self.a


fibonacciNumbers = Fibonacci(10)
for number in fibonacciNumbers:
    print(number)