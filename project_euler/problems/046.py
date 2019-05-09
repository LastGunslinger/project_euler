prompt = '''

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

from itertools import count
from logging import Logger
from typing import Iterable

from project_euler.utilities import is_odd, is_prime, primes


def composites() -> Iterable[int]:
    for x in count(9):
        if is_odd(x) and not is_prime(x):
            yield x


def conjecture(number: int) -> bool:
    for prime in primes(number):
        remainder = number - prime
        for x in count(1):
            if 2 * (x ** 2) < remainder:
                continue
            elif 2 * (x ** 2) > remainder:
                break
            else:
                print(f'{number} = {prime} + 2 * {x}^2')
                return True
    return False


def solve(logger: Logger) -> int:
    logger.debug(prompt)

    for number in composites():
        if not conjecture(number):
            print(f'{number} is not equal to the sum of a prime and twice a square')
            return number
