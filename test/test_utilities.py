import project_euler.utilities as utils
import math


def test_fibonacci():
    assert list(utils.fibonacci(10)) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_sieve_of_erastosthenes():
    assert list(utils.sieve_of_eratosthenes(10)) == [2, 3, 5, 7]


def test_factors():
    assert sorted(utils.factors(28)) == [1, 2, 4, 7, 14, 28]
    # assert sorted(utils.new_factors(28, prime=True)) == [2, 7]
    assert sorted(utils.factors(9)) == [1, 3, 9]
    # assert sorted(utils.new_factors(9, prime=True)) == [3]


def test_divides():
    assert set(utils._divides(24, [2, 3])) == set([(2, 3), (3, 1)])


def test_prime_factors_recursive():
    assert sorted(utils.prime_factors_recursive(644)) == [2, 2, 7, 23]
    # assert sorted(utils.new_factors(28, prime=True)) == [2, 7]
    assert sorted(utils.prime_factors_recursive(645)) == [3, 5, 43]
    assert sorted(utils.prime_factors_recursive(math.factorial(12))) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 7, 11]
    # assert sorted(utils.new_factors(9, prime=True)) == [3]


def test_prime_factors():
    assert set(utils.prime_factors(644)) == {(2, 2), (7, 1), (23, 1)}
    assert set(utils.prime_factors(645)) == {(3, 1), (5, 1), (43, 1)}
    assert set(utils.prime_factors(math.factorial(12))) == {(2, 10), (3, 5), (5, 2), (7, 1), (11, 1)}


def test_list_to_int():
    assert utils.list_to_int([3, 2, 1]) == 321


def test_int_to_list():
    assert utils.int_to_list(321) == [3, 2, 1]


def test_solve_quadratic():
    assert utils.solve_quadratic(2, -5, -3) == (3, -0.5)
