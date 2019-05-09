prompt = '''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
from project_euler.utilities import primes


def solve():
    logger.debug(prompt)
    limit = 10001
    for index, prime in enumerate(primes()):
        print(f'{index + 1:05}: {prime}')
        if index == limit - 1:
            return prime
