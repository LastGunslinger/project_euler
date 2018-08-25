prompt = '''

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def solve(logger):
    logger.debug(prompt)
    a = 1
    b = a + 1
    while a < b:
        b = a + 1
        c = 1000 - a - b
        while b < c:
            if a * a + b * b == c * c:
                print(f'{a}^2 * {b}^2 = {c}^2 = {c**2}')
                return a * b * c
            else:
                b += 1
                c = 1000 - a - b
        a += 1
