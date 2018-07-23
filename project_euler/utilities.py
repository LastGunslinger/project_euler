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


def primes(start: int=1, stop: typ.Optional[int]=None):
    yield 2
    if start % 2 == 0:
        start += 1
    for num in itertools.count(start=start, step=2):
        if stop and num >= stop:
            raise StopIteration
        if is_prime(num):
            yield num


def factors(number: int) -> int:
    for x in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % x == 0:
            yield x


def fibonacci(n: int=0, stop: int=0) -> int:
    '''
    Return the nth number in the Fibonacci sequence.
    If no n is given, count indefinitely
    '''
    print('well hello')
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
