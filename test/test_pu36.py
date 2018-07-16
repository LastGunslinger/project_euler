from project_euler import pu_35


def test_rotations():
    assert list(pu_35.rotations(179)) == [
        179,
        791,
        917,
    ]