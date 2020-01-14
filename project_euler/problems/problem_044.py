prompt = '''

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
'''
from itertools import count

import project_euler.utilities as utils


def pentagonal(n: int):
    return n * (3 * n - 1) / 2


def is_pentagonal(p: int):
    result = utils.solve_quadratic(3, -1, -2 * p)
    if result[0] == int(result[0]):
        return True
    else:
        return False


async def solve(logger):
    assert is_pentagonal(145)
    assert not is_pentagonal(48)
    assert pentagonal(10) == 145
    logger.debug(prompt)
    for n in count(2):
        p1 = pentagonal(n)
        for x in range(1, n):
            p2 = pentagonal(x)
            # logger.debug(f'P{n} = {p1}, P{x} = {p2}')
            if is_pentagonal(p1 - p2) and is_pentagonal(p1 + p2):
                d = abs(p1 - p2)
                logger.debug(f'D = {d}')
                return d
