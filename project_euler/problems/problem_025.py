'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
import time
import pytest

def solve(digit_limit):
	fm, fn = 1, 1
	fib_index = 2
	fib_number = 2
	while len(str(int(fib_number))) < digit_limit :
		fib_number = fm + fn
		len(str(print(fib_number)))
		fm = fn
		fn = fib_number
		fib_index += 1
	return fib_index

def test_main():
	assert main(3) == 12

if __name__ == '__main__':
	start = time.time()
	print(main(1000))
	print('--- {} seconds ---'.format(time.time()-start))