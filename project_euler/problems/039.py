prompt = '''

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

Perimeter of a right-angled triangle:
p = a + b + (a^2 + b^2)^0.5
'''


def solve():
    logger.debug(prompt)
    results = {}
    for a in range(1, 1000):
        for b in range(1, a):
            perimeter = a + b + (a**2 + b**2)**0.5
            if perimeter > 1000:
                break
            elif perimeter == int(perimeter):
                results[perimeter] = results.get(perimeter, 0) + 1
                logger.debug(f'{perimeter} : a={a}, b={b}, c={(a**2 + b**2)**0.5}')
            else:
                continue
    results = sorted(results, key=results.get, reverse=True)
    logger.debug(results[0])
    return results[0]
