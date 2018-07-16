from project_euler.pu_33 import fraction_reduce, naive_fraction_reduce
import fractions


def test_naive_fraction_reduce():
    assert naive_fraction_reduce(49, 98) == (4, 8)
