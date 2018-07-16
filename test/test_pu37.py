from project_euler import pu_37, primes


def test_truncatable_prime():
    assert primes.is_prime(3797)
    assert pu_37.truncatable_prime(3797)
