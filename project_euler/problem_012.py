'''

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

'''
import time
import math

def solve():
	start = 7
	divisors = []
	while len(divisors) < 500 :
		tri = triangle(start)
		divisors = factors(tri)
		print(f'{tri} has {len(divisors)} divisors')
		start += 1
	print(divisors)
	return tri

def triangle(num):
	result = 0
	for x in range(1, num):
		result += x
	return result

def factors(num):
	results = [1, num]
	if num <= 3:
		return results
	for x in range(2, int(math.sqrt(num) + 1)):
		if num % x == 0:
			results.append(x)
			results.append(int(num/x))
	return sorted(results)

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))