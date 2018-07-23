'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import time
import pytest

def solve(permutation, count):
	permutation_count = 1
	while permutation_count < count :
		permutation = next_permutation(permutation)
		print(permutation)
		permutation_count += 1
	return ''.join([str(x) for x in permutation])

def next_permutation(permutation):
	# Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
	k = find_k(permutation)
	if k is None:
		return None
	# Find the largest index l greater than k such that a[k] < a[l].
	l = find_l(permutation, k)
	# Swap the value of a[k] with that of a[l].
	permutation = swap(permutation, k, l)
	# Reverse the sequence from a[k + 1] up to and including the final element a[n].
	next_permutation = reverse_seq(permutation, k)
	return next_permutation

def find_k(permutation):
	for k in range(len(permutation) - 2, -1, -1):
		if permutation[k] < permutation[k + 1]:
			return k
	return None

def find_l(permutation, k):
	for l in range(len(permutation) - 1, k, -1):
		if permutation[k] < permutation[l]:
			return l

def swap(permutation, index_a, index_b):
	swapped_permutation = list(permutation)
	swapped_permutation[index_a] = permutation[index_b]
	swapped_permutation[index_b] = permutation[index_a]
	return swapped_permutation

def reverse_seq(permutation, k):
	return permutation[:k + 1] + permutation[len(permutation) - 1: k: -1]

def test_main():
	base = [0, 1, 2, 3, 4]
	assert find_k(base) == 3
	assert find_l(base, 3) == 4
	assert swap(base, 3, 4) == [0, 1, 2, 4, 3]
	assert reverse_seq([0, 1, 2, 4, 3], 3) == [0, 1, 2, 4, 3]
	assert main([0, 1, 2], 4) == '120'

if __name__ == '__main__':
	start = time.time()
	print(main([0,1,2,3,4,5,6,7,8,9], 1000000))
	print('--- {} seconds ---'.format(time.time()-start))