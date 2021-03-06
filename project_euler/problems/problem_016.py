prompt = '''

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''
from ..utilities import int_list


async def solve(logger):
    logger.debug(prompt)
    return sum(int_list(2 ** 1000))
