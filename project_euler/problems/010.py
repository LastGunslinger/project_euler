prompt = '''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from project_euler.utilities import primes


def solve():
    logger.debug(prompt)
    limit = 2000000
    prime_sum = 0
    for prime in primes(stop=limit):
        print(prime)
        prime_sum += prime
    return prime_sum