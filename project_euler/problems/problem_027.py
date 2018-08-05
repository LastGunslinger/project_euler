'''
Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41

is clearly divisible by 41.

The incredible formula n^2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2+an+b

, where |a|<1000 and |b|≤1000

where |n|
is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a
and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

##### Assumptions #####
1. Consecutive primes are always counted starting from n = 0
2. Assuming point 1 is true, b can never be an even number > 2
3. Assuming point 1 is true, b can never be negative

'''
from ..utilities import is_prime, primes, is_even
from itertools import count


def quadratic(n, a, b):
    return (n ** 2) + (a * n) + b


def gen_solutions(a: int, b: int):
    for n in count(start=0):
        if n == abs(b):
            raise StopIteration
        yield quadratic(n, a, b)


def solve():
    a_range = range(-1000 + 1, 1000 + 1)
    b_range = range(-1000, 1000 + 1)
    max_prime_count = 0
    coeffs = (None, None)
    for a in a_range:
        prime_count = 0
        for b in b_range:
            for solution in gen_solutions(a, b):
                # if solution in all_primes:
                if is_prime(solution):
                    prime_count += 1
                else:
                    break
            print(f'x^2 + ({a})x + ({b}) returns {prime_count} primes')
            if prime_count > max_prime_count:
                max_prime_count = prime_count
                coeffs = (a, b)

    return coeffs[0] * coeffs[1]
