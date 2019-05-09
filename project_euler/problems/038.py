prompt = '''

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''
import typing as typ
from project_euler.utilities import int_to_list, list_to_int


def is_pandigital(number: typ.Union[int, typ.List[int]]) -> bool:
    if isinstance(number, int):
        number = int_to_list(number)
    if 0 in number:
        return False
    elif len(number) != 9:
        return False
    elif len(number) != len(set(number)):
        return False
    else:
        return True


def concatenated_product(number: int) -> int:
    cat_product = int_to_list(number)
    count = 2
    while len(cat_product) < 9:
        cat_product += int_to_list(number * count)
        count += 1

    if is_pandigital(cat_product):
        return list_to_int(cat_product)
    else:
        return None


def solve():
    logger.debug(prompt)
    result = []
    # Range only goes up to the largest pandigital 4-digit number
    for x in range(9877):
        product = concatenated_product(x)
        if product:
            logger.debug(f'Pandigital: {product}')
            result.append(product)
    return max(result)
