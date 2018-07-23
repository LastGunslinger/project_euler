import importlib
import sys
import time
import typing as typ

from termcolor import colored


def run(args: typ.List[typ.Any]):
    if len(args) < 2:
        sys.exit('No problem given!')
    else:
        for arg in args[1:]:
            problem = importlib.import_module(f'project_euler.problems.{arg}')
            start = time.time()
            print(f'--- {arg} ---')
            yield arg, problem.solve(), time.time() - start


for arg, result, elapsed in run(sys.argv):
    print(f'--- Summary ---')
    print(f'Result  : {colored(result, "green")}')
    print(f'Elapsed : {colored(elapsed, "yellow")} seconds')
    print('-------------------')
