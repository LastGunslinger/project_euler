prompt = '''

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from project_euler.utilities import factors


def solve():
    logger.debug(prompt)
    amicables = set()
    for number in range(1, 10000):
        divisor_sum = sum(factors(number, proper=True))
        if sum(factors(divisor_sum, proper=True)) == number and number != divisor_sum:
            amicables.add(number)
            amicables.add(divisor_sum)
            print(f'{number}, {divisor_sum}')
    return sum(amicables)
