from project_euler import checker


def test_get_solution():
    assert checker._get_solution(1) == 233168
    assert checker._get_solution(2) == 4613732
