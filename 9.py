'''

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''
import time

def main():
	a = 1
	b = a + 1
	while a < b:
		b = a + 1
		c = 1000 - a - b
		while b < c :
			if a*a + b*b == c*c:
				print(a, b, c)
				return a*b*c
			else:
				b += 1
				c = 1000 - a - b
		a += 1

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))