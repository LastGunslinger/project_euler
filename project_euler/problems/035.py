prompt = '''

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''
from project_euler.utilities import primes, is_prime, int_list


def rotations(number: int) -> int:
    number = int_list(number)
    if len(number) == 1:
        yield number[0]
        raise StopIteration
    for x in range(1, len(number)):
        rotation = number[x:] + number[:x]
        yield sum(digit * (10 ** (len(rotation) - 1 - index)) for index, digit in enumerate(rotation))


def solve():
    logger.debug(prompt)
    # Prefill set with known circular primes
    result = {2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97}
    for prime in primes(stop=1000000):
        if prime in result:
            continue
        prime_rotations = [prime]
        for rotation in rotations(prime):
            if is_prime(rotation):
                prime_rotations.append(rotation)
            else:
                break
        else:
            logger.debug(f'Circular Primes Found: {prime_rotations}')
            result.update(prime_rotations)
    # print(sorted(result))
    return len(result)
