import importlib
import logging
import sys
import time
import typing as typ
from project_euler.checker import check_solution
from pathlib import Path
import asyncio

from termcolor import colored


async def solve(problem_name):
    # print(f'--- {arg} ---')
    problem = importlib.import_module(
        f'project_euler.problems.{problem_name}')
    # Set global logger settings
    logger = logging.getLogger(f'{__name__}.{problem_name}')
    logger.setLevel(logging.DEBUG)
    # Setup file handler for this problem
    file_handler = logging.FileHandler(
        f'{Path(Path.cwd(), "logs", problem_name)}.log', mode='w')
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
    solution = await problem.solve(logger)
    correct = await check_solution(problem_name[-3:], solution)
    elapsed = time.time() - start
    logger.debug(f'SOLUTION = {solution}')
    logger.debug(f'SOLUTION TIME = {elapsed} s')
    return problem_name, solution, elapsed, correct


async def async_main():
    if len(sys.argv) <= 1:
        problem_dir = Path(Path.cwd(), 'project_euler/problems')
        problem_names = [x.stem for x in problem_dir.iterdir() if x.suffix == '.py']
    else:
        problem_names = sys.argv[1:]

    problem_tasks = [asyncio.create_task(solve(x)) for x in problem_names]

    print(f'Solving {len(problem_tasks)} Euler problems...')
    for task in asyncio.as_completed(problem_tasks):
        try:
            problem, solution, elapsed, correct = await task
            print(f'{problem.upper()} ({round(elapsed, 2)} s) : {colored(solution, "green" if correct else "red")}')
        except Exception as exc:
            print(exc)

asyncio.run(async_main())
