prompt = '''

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
'''
import typing as typ
from itertools import permutations

import project_euler.utilities as utils


def divisive(numbers: typ.List[int], primes: typ.List[int]):
    for index, prime in enumerate(primes, 1):
        partial = utils.list_to_int(numbers[index:index + 3])
        if partial % prime:
            return False
    return True


def solve():
    logger.debug(prompt)
    number = list(range(0, 10))
    primes = list(utils.primes(17))
    divisive_nums = []
    assert divisive(utils.int_to_list(1406357289), primes)
    for num in permutations(number):
        if num[0] == 0:
            continue
        if num[3] % 2:
            continue
        if num[4] % 3:
            continue
        if num[5] % 5:
            continue
        # logger.debug(f'Permutation: {num}')
        if divisive(num, primes):
            logger.debug(f'Divisive Number Found: {num}')
            divisive_nums.append(utils.list_to_int(num))

    assert 1406357289 in divisive_nums
    return sum(divisive_nums)
