prompt = '''

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''


def solve():
    logger.debug(prompt)
    target_value = 200
    coin_values = [1, 2, 5, 10, 20, 50, 100, 200]

    return count_combinations(coin_values, int(len(coin_values) / coin_values[0]), target_value)


def count_combinations(coin_values, index, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if index <= 0 and total >= 1:
        return 0
    return count_combinations(coin_values, index - 1, total) + count_combinations(coin_values, index, total - coin_values[index - 1])
