prompt = '''

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''
from functools import reduce
from itertools import count

from project_euler.utilities import int_list


def solve():
    logger.debug(prompt)
    limit = 1000000
    decimal = [0]
    for number in count(1):
        decimal += int_list(number)
        if len(decimal) > limit:
            break
    result = [decimal[10**x] for x in range(7)]
    logger.debug(result)
    return reduce(lambda x, y: x * y, result)
