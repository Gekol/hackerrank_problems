from problems import compare_triplets


def test_one():
    assert(compare_triplets([5, 6, 7], [3, 6, 10]), [1, 1])


def test_two():
    assert(compare_triplets([1, 3, 2], [1, 3, 2]), [0, 0])


def test_three():
    assert(compare_triplets([2, 5, 3], [1, 4, 5]), [2, 1])
