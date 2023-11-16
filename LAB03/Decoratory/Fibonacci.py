import timeit
from functools import lru_cache


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@lru_cache(maxsize=128)
def fibonacci2(n):
    if n <= 1:
        return n
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)


print(timeit.timeit("fibonacci(10)", setup="from __main__ import fibonacci", number =10**6))
print(timeit.timeit("fibonacci2(10)", setup="from __main__ import fibonacci2", number =10**6))

