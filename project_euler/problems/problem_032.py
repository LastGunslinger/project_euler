prompt = '''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
from logging import Logger
from ..utilities import int_list, int_set


def possibly_pandigital(num: int) -> bool:
    num_set = int_set(num)
    if 0 in num_set:
        return False
    if len(num_set) != len(str(num)):
        return False
    else:
        return True


def is_pandigital(*numbers: int) -> bool:
    number_list = int_list(*numbers)
    number_set = int_set(*numbers)
    if 0 in number_set:
        return False
    elif len(number_set) != 9:
        return False
    elif len(number_list) != len(number_set):
        return False
    else:
        return True


def solve(logger: Logger) -> int:
    logger.debug(prompt)
    # Mathematically, pandigitals can be created with 2 * 3 digit numbers or 1 * 4 digit numbers.
    # This reduces the range of numbers I need to look for.

    # First, find all 2 digit non-repeating numbers with no zero
    pandigital_products = set()
    a_numbers = range(1, 988)
    # b_numbers = list(range(123, 9877))

    for a_number in a_numbers:
        if 0 in int_set(a_number):
            continue
        elif a_number < 10:
            b_numbers = list(range(1234, 9877))
        elif a_number < 100:
            if str(a_number)[0] == str(a_number)[1]:
                continue
            b_numbers = list(range(123, 988))
        else:
            if str(a_number)[0] == str(a_number)[1] or str(a_number)[1] == str(a_number)[2]:
                continue
            b_numbers = list(range(123, a_number))

        for b_number in b_numbers:
            product = a_number * b_number
            if is_pandigital(a_number, b_number, product):
                logger.debug(f'{a_number} * {b_number} = {product}')
                pandigital_products.add(product)

    return sum(pandigital_products)
