from project_euler.utilities import sieve_of_eratosthenes as soe


def test_sieve_of_erastosthenes():
    assert [x for x in soe(10)] == [2, 3, 5, 7]
