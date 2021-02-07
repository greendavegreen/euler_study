from factoring import factor


def test_factor():
    assert [5, 7, 13, 29] == list(factor.factor(13195))


def test_multi_factor():
    assert [7, 7] == list(factor.factor(49))
