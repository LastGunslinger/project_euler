'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''

def main():
	factors = []
	maximum = 600851475143
	i = 2
	while i <= maximum:
		if is_factor(i, maximum):
			factors.append(i)
			maximum = maximum / i
			i = 2
		else:
			i += 1
	return max(factors)

def is_factor(small_num, large_num):
	if large_num % small_num == 0:
		return True
	return False


if __name__ == '__main__':
	print(main())