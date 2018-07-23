'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
from .utilities import primes


def solve():
    limit = 10001
    for index, prime in enumerate(primes()):
        print(f'{index + 1:05}: {prime}')
        if index == limit - 1:
            return prime
