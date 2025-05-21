from problems import sum_func


def test_one():
    assert(sum_func(2, 3), 5)


def test_two():
    assert(sum_func(15, -7), 8)


def test_three():
    assert(sum_func(100, 1011), 1111)
