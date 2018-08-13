prompt = '''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import typing as typ

from ..utilities import int_list, primes


def is_pandigital(number: typ.Union[int, typ.List[int]]) -> bool:
    if isinstance(number, int):
        number = int_list(number)
    if 0 in number:
        return False
    elif len(number) != len(set(number)):
        return False
    else:
        return True


def solve(logger):
    logger.debug(prompt)
    for prime in sorted(primes(987654321), reverse=True):
        if is_pandigital(prime):
            logger.debug(prime)
            return prime
