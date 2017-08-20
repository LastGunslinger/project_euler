from itertools import count

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
			for prime in self.prime_list:
				if self._count % prime == 0:
					is_prime = False
					break
			if is_prime:
				self.prime_list.append(self._count)
				return self._count
			
		
