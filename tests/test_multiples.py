import factoring.multiples as mult


def test_multiples():
    assert sorted(mult.multiples([3, 5], 10)) == [3, 5, 6, 9]
