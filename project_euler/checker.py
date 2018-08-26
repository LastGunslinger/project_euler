import requests as req
import re
import typing as typ


def _get_solution(problem: int):
    '''Pull the solution from the luckytoilet solution repo'''
    url = 'https://raw.githubusercontent.com/luckytoilet/projecteuler-solutions/master/Solutions.md'
    with req.get(url) as resp:
        if resp.status_code == 200:
            match = re.search(fr'^{problem}\.\s(?P<solution>[\-\.\d]+)', resp.text, re.MULTILINE)
        else:
            raise Exception(f'Response {resp.status_code} - could not connect to checker GitHub page.')

        if match:
            return float(match.group('solution'))
        else:
            message = f'Solution not found for problem {problem}'
            raise Exception(message)


def check_solution(problem: typ.Union[int, str], solution: int):
    if isinstance(problem, str):
        problem = int(problem)
    try:
        return float(solution) == float(_get_solution(problem))
    except Exception as exc:
        print(exc)
        return False
