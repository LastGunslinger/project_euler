import itertools
import math
import pytest
from typing import Optional

class PrimeIterator:
    def __init__(self, sentinel=None):
        self.prime_list = []
        self._count = 1
        self.sentinel = sentinel

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self._count += 1
            if self.sentinel and self._count >= self.sentinel:
                raise StopIteration
            for prime in [x for x in self.prime_list if x < math.sqrt(self._count) + 1]:
                if self._count % prime == 0:
                    break
            else:
                self.prime_list.append(self._count)
                print(self._count)
                return self._count


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


def gen_primes(start: int=1, stop: Optional[int]=None):
    if start % 2 == 0:
        start += 1
    for num in itertools.count(start=start, step=2):
        if stop and num >= stop:
            raise StopIteration
        if is_prime(num):
            yield num


def test_gen_primes():
    for x in gen_primes():
        print(x)
        if x > 50:
            break


@pytest.mark.parametrize("test_input, expected", [
    (2, True),
    (3, True),
    (5, True),
    (17, True),
    (25, False),
    (101, False),
])

def test_is_prime(test_input, expected):
    is_prime(test_input)
