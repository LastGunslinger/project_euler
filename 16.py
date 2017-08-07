'''

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''
import time
import math

def main():
	power = str(int(math.pow(2, 1000)))
	print(power)
	result = 0
	for num in power:
		result += int(num)
	return result

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))