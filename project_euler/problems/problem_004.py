'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
from .utilities import int_list


def solve():
    palindromes = []
    # loop backwards through n * m for 100 <= m <= n <= 1000
    for m in reversed(range(100, 1000)):
        for n in reversed(range(100, 1000)):
            product = m * n
            if int_list(product) == int_list(product)[::-1]:
                palindromes.append(product)
    return max(palindromes)
