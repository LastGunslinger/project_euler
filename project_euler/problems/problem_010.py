prompt = '''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from ..utilities import primes


async def solve(logger):
    logger.debug(prompt)
    limit = 2000000

    return sum(primes(limit=limit))
