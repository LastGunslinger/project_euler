'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''
import time
import pytest

def main(target_value):
	coin_values = { 2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 }
	coin_amounts = [0] * len(coin_values)
	combinations = []

	for coin in coin_values:
		

	return

def test_main():
	pass

if __name__ == '__main__':
	start = time.time()
	print(f'Result: {main()}')
	print('--- {} seconds ---'.format(time.time()-start))