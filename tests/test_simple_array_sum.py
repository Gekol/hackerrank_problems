from problems import arr_sum


def test_one():
    assert(arr_sum([1, 2, 3, 4, 10, 11]), 31)


def test_two():
    assert(arr_sum([1, 2, 3, -3, -1, -2, 10]), 10)


def test_three():
    assert(arr_sum([0, 10, 15, 35, 25, -60]), 25)
