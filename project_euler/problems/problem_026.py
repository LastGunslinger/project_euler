prompt = '''

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
import re
import typing as typ

from ..utilities import int_list


async def solve(logger):
    logger.debug(prompt)
    limit = 1000
    longest_recurring = 2
    recurring_length = 1
    for number in range(2, limit):
        q, new_len = repeats(1, number)
        logger.debug(f'1 / {number} : {new_len} : {q}')
        if new_len > recurring_length:
            logger.debug(f'1 / {number} : {new_len} : {q}')
            if new_len > recurring_length:
                recurring_length = new_len
                longest_recurring = number

    logger.debug(f'1 / {longest_recurring} : {recurring_length}')
    return longest_recurring


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

        if len(quotient) > divisor * 2:
            pattern = find_pattern(quotient)
            return pattern, len(pattern) if pattern else 0

    return quotient, 0


def find_pattern(seq: typ.List[int], min_len: int=1) -> int:
    seq = seq.copy()

    seq = ''.join([str(x) for x in seq])
    seq = re.sub(r'\A0+', '', seq, count=1)
    match = re.search(r'(?P<repeat>\d+)\1+', seq)
    if match:
        repeating_group = [int(x) for x in match.group('repeat')]
        for rotation in range(1, len(repeating_group) + 1):
            rotated_group = rotate(repeating_group, rotation)
            # logger.debug(rotated_group)
            if rotated_group == repeating_group:
                return repeating_group[:rotation]
        else:
            return repeating_group
    else:
        return None


def rotate(lst: typ.Iterable, n: int=1) -> typ.Iterable:
    return lst[-(n % len(lst)):] + lst[:-(n % len(lst))]
