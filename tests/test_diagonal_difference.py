from problems import absolute_diagonal_difference


def test_one():
    assert(absolute_diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]), 15)


def test_two():
    assert(absolute_diagonal_difference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]), 2)


def test_three():
    assert(absolute_diagonal_difference([[2, 5], [1, 4]]), 0)
