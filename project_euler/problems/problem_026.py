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
    limit = 1000
    longest_recurring = 2
    recurring_length = 1
    for number in range(2, limit):
        q, new_len = repeats(1, number)
        # q, new_len = find_pattern(q, min_len=recurring_length)
        print(f'1 / {number} : {new_len} : {q}')
        if new_len > recurring_length:
            print(f'1 / {number} : {new_len} : {q}')
            if new_len > recurring_length:
                recurring_length = new_len
                longest_recurring = number

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

'''
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
'''


def repeats(dividend: typ.Union[typ.List[int], int], divisor: int) -> int:
    if isinstance(dividend, int):
        dividend = int_list(dividend)

    quotient = []
    while not (dividend[0] == 0 and len(dividend) == 1):
        if divisor > dividend[0] and len(dividend) > 1:
            dividend[0] = int(str(dividend[0]) + str(dividend.pop(1)))
            quotient.append(0)
            # yield from divide(dividend, divisor)
        elif divisor > dividend[0] and len(dividend) == 1:
            dividend[0] *= 10
            quotient.append(0)
            # yield from divide(dividend, divisor)
        else:
            q = int(dividend[0] / divisor)
            remainder = dividend[0] % divisor
            dividend[0] = remainder
            if len(dividend) == 1 and dividend[0] != 0:
                dividend[0] *= 10
            quotient.append(q)
            # yield from divide(dividend, divisor)
        
        pattern = find_pattern(quotient)
        if pattern:
            return pattern, len(pattern)

    return quotient, 0


def find_pattern(seq: typ.List[int], min_len: int=1) -> int:
    seq = seq.copy()
    '''
    while seq and seq[0] == 0:
        seq.pop(0)
    if len(seq) < 2:
        return 0

    start_index = 0
    mid_index = int(len(seq) / 2)
    while start_index < mid_index < len(seq):
        if seq[start_index:mid_index] == seq[mid_index:mid_index + (mid_index - start_index)]:
            return len(seq[start_index:mid_index])
        else:
            start_index += 1

    return 0
    '''

    seq = ''.join([str(x) for x in seq])
    seq = re.sub(r'\A0+', '', seq, count=1)
    match = re.match(r'\A[0-9]+(?P<repeat>\d+)\1\1\Z', seq)
    if match:
        return [x for x in match.group('repeat')]
    else:
        return None



