from loguru import logger

from project_euler.utilities import prime_factors


prompt = '''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def solve():
    logger.debug(prompt)
    number = 600851475143
    return sorted(
        prime_factors(number),
        key=lambda x: x[0],
        reverse=True
    )[0][0]
