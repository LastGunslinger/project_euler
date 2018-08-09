prompt = '''

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

Things to keep in mind:
1) Numerator and denominator are 2 digits
2) Fraction is < 1
3) Multiples of 10 are considered trivial
'''

import fractions
from functools import reduce
from typing import Tuple


def fraction_reduce(num: int, denom: int) -> Tuple[int]:
    gcd = fractions.gcd(num, denom)
    if gcd > 1:
        return num / gcd, denom / gcd,
    else:
        return num, denom


def naive_fraction_reduce(num: int, denom: int) -> Tuple[int]:
    num_str = str(num)
    denom_str = str(denom)
    for number in range(9, 0, -1):
        if str(number) in num_str and str(number) in denom_str:
            num_str = num_str.replace(str(number), '', 1)
            denom_str = denom_str.replace(str(number), '', 1)
            return fraction_reduce(int(num_str), int(denom_str))
    else:
        return num, denom


def generate_fractions():
    for denominator in range(10, 100):
        for numerator in range(10, denominator):
            yield numerator, denominator


def solve(logger):
    logger.debug(prompt)
    naive_fractions = []
    for num, denom in generate_fractions():
        reduced = fraction_reduce(num, denom)
        naive_reduced = naive_fraction_reduce(num, denom)
        if reduced == naive_reduced and reduced != (num, denom):
            logger.debug(f'Naive fraction: {num} / {denom}')
            naive_fractions.append((num, denom))
    assert len(naive_fractions) == 4

    num_product = reduce(lambda x, y: x * y, [x[0] for x in naive_fractions])
    denom_product = reduce(lambda x, y: x * y, [x[1] for x in naive_fractions])
    logger.debug(f'Product Fraction: {int(num_product)} / {int(denom_product)}')
    product_fraction = fraction_reduce(num_product, denom_product)
    logger.debug(f'Reduced Product Fraction: {int(product_fraction[0])} / {int(product_fraction[1])}')
    return int(product_fraction[1])
