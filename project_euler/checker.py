import requests as req
import re
import typing as typ


def _get_solution(problem: int):
    '''Pull the solution from the luckytoilet solution repo'''
    url = 'https://raw.githubusercontent.com/luckytoilet/projecteuler-solutions/master/Solutions.md'
    with req.get(url) as resp:
        match = re.search(fr'.*\s{problem}\.\s(?P<solution>\d+)', resp.text)
        try:
            return int(match.group('solution'))
        except Exception:
            message = f'Solution not found for problem {problem}'
            print(message)
            raise Exception(message)


def check_solution(problem: typ.Union[int, str], solution: int):
    if isinstance(problem, str):
        problem = int(problem)
    try:
        return solution == _get_solution(problem)
    except Exception:
        return False
