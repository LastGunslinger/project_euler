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
from typing import List


def solve():
    assert divide(1, 11) == 2
    assert divide(1, 12) == 1
    limit = 1000
    value = 7
    longest_recurring = 6
    for x in range(11, limit):
        recurring_length = divide(1, x)
        print(f'1 / {x} : {recurring_length}')
        if recurring_length > longest_recurring:
            longest_recurring = recurring_length
            value = x
    return value


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


def divide(dividend: int, divisor: int):
    dividend = int_list(dividend)
    quotient = []

    while True:
        while divisor > dividend[0]:
            if len(dividend) > 1:
                dividend[0] = int(str(dividend[0]) + str(dividend.pop(1)))
            else:
                dividend[0] *= 10
                quotient.append(0)

        quotient.append(int(dividend[0] / divisor))
        remainder = dividend[0] % divisor
        if remainder:
            dividend[0] -= (divisor * int(dividend[0] / divisor))
            seq = seq_len(quotient)
            if seq:
                return seq
        else:
            return 0


def guess_seq_len(seq: List[int]) -> int:
    guess = None
    max_len = int(len(seq) / 2)
    for x in range(2, max_len):
        if seq[0:x] == seq[x:2 * x]:
            guess = x

    return guess


def seq_len(seq: int) -> int:
    # print(seq)
    search_str = ''.join(str(x) for x in seq)
    match = re.search(r'0+(?P<repeat>\d+)(\1)', search_str)
    if match:
        print(match.group('repeat'))
        return len(match.group('repeat'))
    else:
        return 0
