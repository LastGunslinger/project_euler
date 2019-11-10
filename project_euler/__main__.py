import importlib
import logging
import sys
import time
import typing as typ
from .checker import check_solution
from pathlib import Path

from termcolor import colored


def run(args: typ.List[typ.Any]):
    if len(args) < 2:
        sys.exit('No problem given!')
    else:
        for arg in args[1:]:
            # print(f'--- {arg} ---')
            problem = importlib.import_module(f'project_euler.problems.{arg}')
            # Set global logger settings
            logger = logging.getLogger(f'{__name__}.{arg}')
            logger.setLevel(logging.DEBUG)
            # Setup file handler for this problem
            file_handler = logging.FileHandler(f'{Path(Path.cwd(), "logs", arg)}.log', mode='w')
            file_handler.setLevel(logging.DEBUG)
            # Setup stream handler for this problem
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.INFO)

            # Setup formatter
            formatter = logging.Formatter('%(asctime)s : %(name)s : %(levelname)s : %(message)s')
            file_handler.setFormatter(formatter)
            formatter = logging.Formatter('%(message)s')
            stream_handler.setFormatter(formatter)
            # Add the handler
            logger.addHandler(file_handler)
            logger.addHandler(stream_handler)

            start = time.time()
            solution = problem.solve(logger)
            elapsed = time.time() - start
            logger.debug(f'SOLUTION = {solution}')
            logger.debug(f'SOLUTION TIME = {elapsed} s')
            yield arg, solution, elapsed


for arg, result, elapsed in run(sys.argv):
    print(f'----- {arg.upper()} SUMMARY ----')
    print(f'Result  : {colored(result, "green" if check_solution(arg[-3:], result) else "red")}')
    print(f'Elapsed : {colored(elapsed, "green" if elapsed < 60 else "red")} seconds')
    print('-------------------')
