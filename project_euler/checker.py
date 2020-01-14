import re
import typing as typ
import aiohttp
import ssl

from os import environ


async def _get_solution(problem: int):
    '''Pull the solution from the luckytoilet solution repo'''
    url = 'https://raw.githubusercontent.com/luckytoilet/projecteuler-solutions/master/Solutions.md'
    ssl_ctx = ssl.create_default_context(cafile=environ['REQUESTS_CA_BUNDLE'])

    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=ssl_ctx) as resp:
            if resp.status == 200:
                match = re.search(fr'^{problem}\.\s(?P<solution>[\-\.\d]+)', await resp.text(), re.MULTILINE)
            else:
                raise Exception(f'Response {resp.status} - could not connect to checker GitHub page.')

            if match:
                return float(match.group('solution'))
            else:
                message = f'Solution not found for problem {problem}'
                raise Exception(message)

    """ with req.get(url, verify=certifi.where()) as resp:
        if resp.status_code == 200:
            match = re.search(fr'^{problem}\.\s(?P<solution>[\-\.\d]+)', resp.text, re.MULTILINE)
        else:
            raise Exception(f'Response {resp.status_code} - could not connect to checker GitHub page.') """


async def check_solution(problem: typ.Union[int, str], solution: int):
    if isinstance(problem, str):
        problem = int(problem)
    try:
        return float(solution) == float(await _get_solution(problem))
    except Exception as exc:
        print(exc)
        return False
