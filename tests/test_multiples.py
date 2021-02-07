import factoring.multiples as mult


def test_multiples():
    assert sorted(mult.multiples([3, 5], 10)) == [3, 5, 6, 9]


def test_lcm():
    assert 2520 == mult.lcm(range(1,10))
