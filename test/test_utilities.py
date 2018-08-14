import project_euler.utilities as utils


def test_sieve_of_erastosthenes():
    assert list(utils.sieve_of_eratosthenes(10)) == [2, 3, 5, 7]


def test_factors():
    assert list(utils.factors(28)) == [1, 2, 4, 7, 14, 28]
    assert list(utils.factors(28, prime=True)) == [2, 7]
    assert list(utils.factors(9)) == [1, 3, 9]
    assert list(utils.factors(9, prime=True)) == [3]


def test_divides():
    assert set(utils._divides(24, [2, 3])) == set([(2, 3), (3, 1)])


def test_prime_factors():
    assert set(utils.prime_factors(24)) == set([(2, 3), (3, 1)])


def test_list_int():
    assert utils.list_int([3, 2, 1]) == 321


def test_int_list():
    assert utils.int_list(321) == [3, 2, 1]


def test_solve_quadratic():
    assert utils.solve_quadratic(2, -5, -3) == (3, -0.5)
