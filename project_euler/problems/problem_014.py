prompt = '''

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
NOTE: RUN FROM THE COMMAND LINE! - To speed this module up, I run in multiprocess mode, which may not work correctly when run in the debugger.
'''
from multiprocessing import Pool
from typing import Tuple


def solve(logger):
    logger.debug(prompt)
    with Pool() as pool:
        chain_counts = pool.map(count_chain, range(2, 1000000))
    return max(chain_counts, key=lambda x: x[1])[0]


def count_chain(number: int) -> Tuple[int]:
    num = number
    count = 1
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (3 * num) + 1
        count += 1
    print(f'{int(number)} -> {count}')
    return (int(number), count)
