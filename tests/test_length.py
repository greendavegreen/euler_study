from sequences.length import n_by_n_palindromes


def test_1_by_1():
    assert 9 == max(n_by_n_palindromes(1))


def test_2_by_2_palindromes():
    assert 9009 == max(n_by_n_palindromes(2))


def test_3_by_3():
    assert 906609 == max(n_by_n_palindromes(3))


def test_4_by_4():
    assert 99000099 == max(n_by_n_palindromes(4))
