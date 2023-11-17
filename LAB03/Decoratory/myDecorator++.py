import os
import pickle
import csv
import timeit

def myDecoratorFormat(format):
    def myDecorator(function):
        def wrapper(n):
            fibonacci_file = f'fibonacci_{n}.{format}'

            # Sprawdzamy, czy wynik jest już zapisany na dysku
            if os.path.exists(fibonacci_file):
                if format == 'pickle':
                    with open(fibonacci_file, 'rb') as file:
                        result = pickle.load(file)
                elif format == 'csv':
                    with open(fibonacci_file, 'r') as file:
                        reader = csv.reader(file)
                        result = next(reader)[0]
                print("existing")
            else:
                # Obliczamy wynik funkcji
                result = function(n)

                # Zapisujemy wynik na dysku
                if format == 'pickle':
                    with open(fibonacci_file, 'wb') as file:
                        pickle.dump(result, file)
                elif format == 'csv':
                    with open(fibonacci_file, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([result])
                print("new")
            return result
        return wrapper
    return myDecorator

@myDecoratorFormat('csv')
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(timeit.timeit("fibonacci(1)", setup="from __main__ import fibonacci", number=1))
print(timeit.timeit("fibonacci(1)", setup="from __main__ import fibonacci", number=1))
