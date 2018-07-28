'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	 = 	0.5
1/3	 = 	0.(3)
1/4	 = 	0.25
1/5	 = 	0.2
1/6	 = 	0.1(6)
1/7	 = 	0.(142857)
1/8	 = 	0.125
1/9	 = 	0.(1)
1/10 = 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
import time
import pytest
import re
import math
from ..utilities import is_prime, int_list
import typing as typ
import re


def solve():
    assert divide(1, 11) == 2
    assert divide(1, 12) == 1
    limit = 1000
    longest_recurring = 2
    recurring_length = 1
    for number in range(2, limit):
        q = []
        for x in divide(1, number):
            q.append(x)
            new_len = pattern_len(q, min_len=recurring_length)
            if new_len > recurring_length:
                print(f'1 / {number} : {new_len} : {q}')
                if new_len > recurring_length:
                    recurring_length = new_len
                    longest_recurring = number
                break
    print(f'1 / {longest_recurring} : {recurring_length}')
    return longest_recurring


    for x in range(1, limit):
        q, length = long_divide(1, x)
        if length > recurring_length:
            recurring_length = length
            longest_recurring = x
            print(f'1 / {x} : {recurring_length}')
    return longest_recurring


def long_divide(dividend, divisor):
    pattern = re.compile(r'(\d+)\1{3,}', re.IGNORECASE)
    quotient = ''
    remainder = 1
    while remainder != 0:
        quotient += str(int(dividend / divisor))
        if quotient == '0':
            quotient += '.'
        remainder = dividend % divisor
        dividend = remainder * 10
        match = pattern.search(quotient)
        if match and quotient[-1] != '0':
            quotient = re.sub(r'{}+'.format(match.group()), r'({})'.format(match.group(1)), quotient)
            # print(match.group(1))
            return quotient, len(match.group(1))
    return quotient, 0


def divide(dividend: typ.Union[typ.List[int], int], divisor: int) -> int:
    if isinstance(dividend, int):
        dividend = int_list(dividend)
    if dividend[0] == 0 and len(dividend) == 1:
        raise StopIteration
    elif divisor > dividend[0] and len(dividend) > 1:
        dividend[0] = int(str(dividend[0]) + str(dividend.pop(1)))
        yield 0
        yield from divide(dividend, divisor)
    elif divisor > dividend[0] and len(dividend) == 1:
        dividend[0] *= 10
        yield 0
        yield from divide(dividend, divisor)
    else:
        q = int(dividend[0] / divisor)
        remainder = dividend[0] % divisor
        dividend[0] = remainder
        if len(dividend) == 1 and dividend[0] != 0:
            dividend[0] *= 10
        yield q
        yield from divide(dividend, divisor)


def pattern_len(seq: typ.List[int], min_len: int=1) -> int:
    seq = ''.join([str(x) for x in seq])
    match = re.match(fr'(?P<repeat>\d+)\1', seq[::-1])
    if match:
        if re.match(r'\A0+\Z', match.group('repeat')):
            return 0
        else:
            return len(match.group('repeat'))
    else:
        return 0



