prompt = '''

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''


def is_palindromic(number: int):
    dec_str = str(number)
    bin_str = str(bin(number))[2:]
    if dec_str == dec_str[::-1] and bin_str == bin_str[::-1]:
        return True
    else:
        return False


def generate_palindromes(start: int=1, stop: int=1000000):
    for number in range(start, stop):
        if is_palindromic(number):
            yield number


async def solve(logger):
    logger.debug(prompt)
    result = set()
    for palindrome in generate_palindromes():
        logger.debug(f'Palindrome Found: {palindrome} : {bin(palindrome)}')
        result.add(palindrome)
    return sum(result)
