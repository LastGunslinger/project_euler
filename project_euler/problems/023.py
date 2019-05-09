prompt = '''

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
from project_euler.utilities import factors


def abundants(limit: int) -> int:
    '''Return all abundant numbers < limit'''
    for number in range(1, limit):
        if sum(factors(number, proper=True)) > number:
            print(f'Abundant: {number}')
            yield number


def solve():
    logger.debug(prompt)
    limit = 28123
    abundant_nums = list(abundants(limit + 1))
    abundant_sums = {x + y for x in abundant_nums for y in abundant_nums if x <= y and x + y <= limit}
    return sum(x for x in range(1, limit + 1) if x not in abundant_sums)
