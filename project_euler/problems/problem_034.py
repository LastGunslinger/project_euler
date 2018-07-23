'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

'''
import time
from math import factorial
from termcolor import colored


def factorial_sum(number: int) -> int:
    result = 0
    for char in str(number):
        digit = int(char)
        result += factorial(digit)
    return result


def largest_digit(number: int) -> int:
    digits = [int(x) for x in list(str(number))]
    return max(digits)


def solve():
    lower_limit = 3
    upper_limit = factorial(9)  # No number can be higher than 9!

    factorial_sums = []
    for x in range(lower_limit, upper_limit + 1):
        if factorial(largest_digit(x)) > x:
            continue
        if x == factorial_sum(x):
            print(f'{"! + ".join(str(x))}! = {x}')
            factorial_sums.append(x)
    return sum(factorial_sums)


if __name__ == '__main__':
    start = time.time()
    print(f'Result: {colored(main(), "green")}')
    print('--- {} seconds ---'.format(time.time() - start))
