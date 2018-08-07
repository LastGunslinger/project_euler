prompt = '''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
from logging import Logger
from ..utilities import int_set


def possibly_pandigital(num: int) -> bool:
    num_set = int_set(num)
    if 0 in num_set:
        return False
    if len(num_set) != len(str(num)):
        return False
    else:
        return True


def is_pandigital(num_1: int, num_2: int) -> bool:
    set_1 = int_set(num_1)
    set_2 = int_set(num_2)
    if set_1.intersection(set_2):
        return False
    if len(set_1) + len(set_2) > 5:
        return False
    else:
        product = num_1 * num_2

        if not possibly_pandigital(product):
            return False
        set_3 = int_set(product)
        if set_3.intersection(set_1) or set_3.intersection(set_2):
            return False
        if len(set_1) + len(set_2) + len(set_3) != 9:
            return False
        else:
            return True


def solve(logger: Logger) -> int:
    logger.debug(prompt)
    # Mathematically, only a 2-digit * 3-digit number can be pandigital.
    # This reduces the range of numbers I need to look for.
    
    # First, find all 2 digit non-repeating numbers with no zero
    pandigital_products = set()
    unique_numbers = list(filter(possibly_pandigital, range(9877)))
    # unique_numbers = [x for x in range(1, 9877) if possibly_pandigital(x)]
    for index, multiplicand in enumerate(unique_numbers):
        for multiplier in unique_numbers[index:]:
            if is_pandigital(multiplicand, multiplier):
                logger.debug(f'{multiplicand} * {multiplier} = {multiplicand * multiplier}')
                pandigital_products.add(multiplicand * multiplier)
                unique_numbers.remove(multiplier)

    return sum(pandigital_products)
