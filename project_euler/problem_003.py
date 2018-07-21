'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''
import math
import time
from itertools import count

def solve(number):
    prime_factors = [x for x in gen_prime_factors(number)]
    print(sorted(prime_factors))
    return max(prime_factors)

def gen_prime_factors(number):
    for x in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % x == 0 and is_prime(x):
            yield x

def test_gen_prime_factors():
    assert [x for x in gen_prime_factors(13195)] == [5, 7, 13, 29]

def is_prime(number):
    if 1 < number < 4:
        return True
    for x in range(2, int(math.ceil(math.sqrt(number))) + 1):
        if number % x == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(4) == False
    assert is_prime(9) == False
    assert is_prime(101) == True

if __name__ == '__main__':
    start = time.time()
    print(main(600851475143))
    print('--- {} seconds ---'.format(time.time()-start))