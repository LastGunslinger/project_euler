prompt = '''

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

2t = n(n + 1)
2t = n^2 + n
n^2 + n -2t = 0
x = -1 +- sqrt(1 - 4)
'''
from itertools import count
from pathlib import Path

from ..utilities import solve_quadratic


def triangle_numbers():
    for x in count(1):
        yield (0.5 * x) * (x + 1)


def is_triangle_number(number: int):
    result, _ = solve_quadratic(1, 1, -2 * number)
    if result == int(result):
        return True
    else:
        return False


def convert_words(filename):
    with open(filename) as f:
        raw_data = f.read().replace('\"', '')
    words = raw_data.split(',')
    word_dict = {}
    for word in words:
        number_val = sum(ord(letter) - 64 for letter in word)
        word_dict[word] = number_val
    return word_dict


async def solve(logger):
    logger.debug(prompt)
    # triangle_number_set = set()
    triangle_words = []
    word_dict = convert_words(Path.cwd() / 'data/problem_042.txt')
    for word, value in word_dict.items():
        if is_triangle_number(value):
            logger.debug(f'{word} : {value}')
            triangle_words.append(word)
    return len(triangle_words)
