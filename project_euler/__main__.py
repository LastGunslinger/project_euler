import importlib
import sys
import time
import typing as typ
from .checker import check_solution
from pathlib import Path

from termcolor import colored
from loguru import logger


def run(args: typ.List[typ.Any]):
    if len(args) < 2:
        sys.exit('No problem given!')
    else:
        for arg in args[1:]:
            # print(f'--- {arg} ---')
            problem = importlib.import_module(f'project_euler.problems.{int(arg):03}')

            logger.add(
                Path.cwd() / f'project_euler/logs/{int(arg):03}.log',
                format='{time:YYYY-MM-DD HH:mm:ss} : {name} : {level} : {message}',
                level='DEBUG'
            )

            start = time.time()
            solution = problem.solve()  # type : ignore
            elapsed = time.time() - start

            yield arg, solution, elapsed


for arg, result, elapsed in run(sys.argv):
    logger.info(f'Result  : {colored(result, "green" if check_solution(arg[-3:], result) else "red")}')
    logger.info(f'Elapsed : {colored(elapsed, "green" if elapsed < 60 else "red")} seconds')
