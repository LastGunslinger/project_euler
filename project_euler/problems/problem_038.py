'''
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

import time
import utilities as utils
from termcolor import colored


def is_pandigital(number: int) -> bool:
    if is_unique(number) and len(str(number)) == 9:
        return True
    else:
        return False


def is_unique(number: int) -> bool:
    num_str = str(number)
    if '0' in num_str:
        return False
    elif len(num_str) == len(set(num_str)):
        return True
    else:
        return False


def concatenate_products(number: int) -> int:
    concatenated_product = str(number)
    count = 2
    while len(concatenated_product) < 9:
        concatenated_product += f'{number * count}'
        count += 1
        if not is_unique(concatenated_product):
            return None
        elif len(concatenated_product) > 9:
            return None
    return int(concatenated_product)


def solve():
    result = []
    for x in range(555555555):
        product = concatenate_products(x)
        if product and is_pandigital(product):
            print(f'Pandigital: {product}')
            result.append(product)
    return max(result)


if __name__ == '__main__':
    start = time.time()
    print(f'Result: {colored(main(), "green")}')
    print('--- {} seconds ---'.format(time.time() - start))
