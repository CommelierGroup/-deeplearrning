import numpy as np

numbers = np.arange(1, 51)

primes = np.array([
    x for x in numbers
    if x > 1 and all(
        x % i != 0
        for i in range(2, int(np.sqrt(x)) + 1)
    )
])

print(primes)
