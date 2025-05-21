from problems import big_sum


def test_one():
    assert(big_sum([1, 2, 3, 4, 10, 11]), 31)


def test_two():
    assert(big_sum([1, 2, 3, -3, -1, -2, 10]), 10)


def test_three():
    assert(big_sum([0, 10, 15, 35, 25, -60]), 25)
