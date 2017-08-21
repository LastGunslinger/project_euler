from itertools import count
import math
import pytest

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
			is_prime = True
			if self.sentinel and self._count >= self.sentinel:
				raise StopIteration
			for prime in [x for x in self.prime_list if x < math.sqrt(self._count) + 1]:
				if self._count % prime == 0:
					is_prime = False
					break
			if is_prime:
				self.prime_list.append(self._count)
				print(self._count)
				return self._count

def is_prime(number):
	if number < 2:
		return False
	for x in range(2, int(math.sqrt(number)) + 1):
		if number % x == 0:
			return False
	return True

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
			
		
