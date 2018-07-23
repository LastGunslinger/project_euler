'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from .utilities import primes


def solve():
    limit = 2000000
    return sum(x for x in primes(stop=limit))
