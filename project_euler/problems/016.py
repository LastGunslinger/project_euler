prompt = '''

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''
from project_euler.utilities import int_to_list


def solve():
    logger.debug(prompt)
    return sum(int_to_list(2 ** 1000))
