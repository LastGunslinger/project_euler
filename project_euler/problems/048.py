from loguru import logger


prompt = '''
'''


def solve() -> int:
    logger.debug(prompt)
    start = 646 + 1
    factor_length = 4
    consecutive_target = 4
    result = []

    for number in count(start):
        factors = list(prime_factors(number))
        if len(factors) == factor_length:
            result.append(number)
            if len(result) > 1:
                print(result)
        elif not len(factors) == factor_length:
            result = []

        if len(result) == consecutive_target:
            break

    for num in result:
        values = [f'{key}^{val}' for key, val in factors]
        print(f'{num} = {" ".join(values)}')
    return result[0]
