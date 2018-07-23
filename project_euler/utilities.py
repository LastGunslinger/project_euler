import itertools
import math
import typing as typ


def int_list(number: int) -> typ.List[int]:
    return [int(x) for x in str(number)]


def int_set(number: int) -> typ.Set[int]:
    return {int(x) for x in str(number)}


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    elif 2 <= number <= 3:
        return True
    for x in range(2, int(math.sqrt(number)) + 1):
        if number % x == 0:
            return False
    else:
        return True


def primes(stop: int=1000000):
    yield from sieve_of_eratosthenes(stop)


def factors(number: int) -> int:
    for x in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % x == 0:
            yield x


def fibonacci(n: int=0, stop: int=0) -> int:
    '''
    Return the nth number in the Fibonacci sequence.
    If no n is given, count indefinitely
    '''
    n1, n2 = 1, 2
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


def sieve_of_eratosthenes(limit: int=1000000):
    sieve = {x: None for x in range(2, limit + 1)}
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
