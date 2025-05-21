from problems import calculate_ratio


def test_one():
    assert(calculate_ratio([1, 1, 0, -1, -1]), [0.400000, 0.400000, 0.200000])


def test_two():
    assert(calculate_ratio([1, 2, 0, -1]), [0.500000, 0.250000, 0.250000])


def test_three():
    assert(calculate_ratio([-4, 3, -9, 0, 4, 1]), [0.500000, 0.333333, 0.166667])
