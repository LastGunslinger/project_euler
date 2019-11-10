import project_euler.utilities as utils


def test_is_prime():
    assert not utils.is_prime(600851475143)


def test_sieve_of_erastosthenes():
    assert list(utils.sieve_of_eratosthenes(10)) == [2, 3, 5, 7]


def test_factors():
    assert list(utils.factors(28)) == [1, 2, 4, 7, 14, 28]
    assert list(utils.factors(28, proper=True)) == [2, 4, 7, 14]
    assert list(utils.factors(9)) == [1, 3, 9]
    assert list(utils.factors(9, proper=True)) == [3]
    assert len(list(utils.factors(500500))) == 96


def test_divides():
    assert set(utils._divides(24, [2, 3])) == set([(2, 3), (3, 1)])


def test_prime_factors():
    assert list(utils.prime_factors(13195, exponents=False)) == [5, 7, 13, 29]
    for x, y in utils.prime_factors(644):
        print(f'{x} ^ {y}')
    assert list(utils.prime_factors(644)) == [
        (2, 2)
        (7, 1)
        (23, 1)
    ]
    assert utils.prime_factors(645) == {
        3: 1,
        5: 1,
        43: 1
    }


def test_list_int():
    assert utils.list_int([3, 2, 1]) == 321


def test_int_list():
    assert utils.int_list(321) == [3, 2, 1]


def test_solve_quadratic():
    assert utils.solve_quadratic(2, -5, -3) == (3, -0.5)
