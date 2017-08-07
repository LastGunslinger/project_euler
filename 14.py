'''

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''
import time

def main():
	longest_chain = (2, 2)
	for start in range(2, 1000000):
		chain_len = len(get_chain(start))
		print(start, chain_len)
		if chain_len > longest_chain[1]:
			longest_chain = (start, chain_len)
	return longest_chain

def get_chain(num):
	chain = [num]
	while num > 1:
		if num % 2 == 0:
			num = num/2
		else:
			num = 3*num + 1
		chain.append(num)
	return chain


if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))