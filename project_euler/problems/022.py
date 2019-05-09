prompt = '''

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
from pathlib import Path
from project_euler import DATA_DIR
from loguru import logger


def name_value(name):
    return sum(ord(x) - 64 for x in name)


def solve():
    logger.debug(prompt)
    with Path(DATA_DIR, 'problem_022.txt').open() as name_file:
        data = name_file.read().replace('\"', '')
        names = data.split(',')

    names_dict = {
        name: name_value(name) * (index + 1) for index, name in enumerate(sorted(names))
    }

    result = sum(val for key, val in names_dict.items())
    logger.info(f'RESULT : {result}')
    return result


if __name__ == '__main__':
    solve()
