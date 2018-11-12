import itertools
import math
import multiprocessing
from typing import Dict, Tuple, List, Set, Iterable, Optional, Union
from collections import defaultdict


def solve_quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    ''' Solve a quadratic using the quadratic formula '''
    try:
        solution_1 = (-b + math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
        solution_2 = (-b - math.sqrt(math.pow(b, 2) - (4 * a * c))) / (2 * a)
    except ValueError:
        print(f'a = {a}, b = {b}, c = {c}')
        raise
    return solution_1, solution_2


def number_of_factors(number: int) -> int:
    return 0


def list_int(integer_list: List[int]) -> int:
    return sum(x * (10 ** index) for index, x in enumerate(integer_list[::-1]))


def int_list(*numbers: int) -> List[int]:
    return [int(x) for number in numbers for x in str(number)]


def int_set(*numbers: int) -> Set[int]:
    return {int(x) for number in numbers for x in str(number)}


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    elif 2 <= number <= 3:
        return True
    elif is_even(number):
        return False
    elif str(number)[-1] == 5:
        return False
    for x in range(3, int(math.sqrt(number)) + 1, 2):
        if number % x == 0:
            return False
    else:
        return True


def is_odd(number: int) -> bool:
    if number % 2:
        return True
    else:
        return False


def is_even(number: int) -> bool:
    return not is_odd(number)


def primes(stop: int = 50000) -> Iterable[int]:
    yield from sieve_of_eratosthenes(stop)


def factors(number: int, proper: bool = False) -> Iterable[int]:
    divisors: Iterable[int] = filter(lambda x: number % x == 0, range(1, int(math.sqrt(number)) + 1))
    divisor_set: Set[int] = set(divisors)
    complements = map(lambda x: int(number / x), divisor_set)
    complement_set: Set[int] = set(complements)
    all_factors = sorted(divisor_set.union(complement_set))

    yield from (x for x in all_factors if x != number and proper)


def prime_factors(number: int, exponents: bool = True) -> Dict[int, int]:
    if is_prime(number):
        return {number: 1}

    prime_factors = {} if is_odd(number) else {2: 0}

    prime_factors.update({x: 0 for x in range(3, int(number / 2), 2) if number % x == 0 and is_prime(x)})
    # return _divides(number, prime_factors) if exponents else prime_factors

    if exponents:
        for divisor in sorted(prime_factors.keys(), reverse=True):
            while number % divisor == 0:
                prime_factors[divisor] += 1
                number /= divisor

    return prime_factors

        
    '''
    factors = [] if number % 2 else [2]
    factors += [x for x in range(3, int(number / 2), 2) if not number % x]
    with multiprocessing.Pool() as pool:
        prime_check = pool.map(is_prime, factors)
        print(type(prime_check))
    p_factors = [x for i, x in enumerate(factors) if prime_check[i]]
    print(p_factors)
    # p_factors = [x for x in factors if is_prime(x)]
    return _divides(number, p_factors) if exponents else p_factors
    '''


def _divides(number: int, prime_divisors: Dict[int, int]) -> Dict[int, int]:
    result = []
    for divisor in sorted(prime_divisors.keys(), reverse=True):
        while number % divisor == 0:
            prime_divisors[divisor] += 1
            number /= divisor
    return prime_divisors


def fibonacci(n: int = 0, stop: int = 0) -> Iterable[int]:
    '''
    Return the nth number in the Fibonacci sequence.
    If no n is given, count indefinitely
    '''
    n1, n2 = 1, 1
    yield n1
    if n and n == 1:
        raise StopIteration
    yield n2
    if n and n == 2:
        raise StopIteration

    for x in itertools.count(2):
        if n and x >= n:
            raise StopIteration
        else:
            fib_sum = n1 + n2
            if stop and fib_sum >= stop:
                raise StopIteration
            yield fib_sum
            n1, n2 = n2, fib_sum


def sieve_of_eratosthenes(limit: int = 1000000) -> Iterable[int]:
    sieve: Dict[int, Optional[bool]] = {x: None for x in range(2, limit + 1)}
    p_value = 2

    while p_value in sieve:
        if sieve[p_value] is None:
            sieve[p_value] = True
            yield p_value
            for x in itertools.count(2):
                key = p_value * x
                if key in sieve:
                    sieve[key] = False
                else:
                    p_value += 1
                    break
        elif sieve[p_value] is False:
            p_value += 1
        else:
            raise StopIteration
