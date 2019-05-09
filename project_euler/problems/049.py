from loguru import logger
from project_euler.utilities import int_to_list, list_to_int


prompt = '''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''


def solve():
    logger.debug(prompt)
    limit = 1000
    result = 0
    for num in range(1, limit + 1):
        result += pow(num, num)
    result_list = int_to_list(result)
    return ''.join(str(x) for x in result_list[-10:])
