from factoring.sieve import nth_prime


def test_nth_prime():
    assert 13 == nth_prime(6)


def test_7th_prime():
    assert 17 == nth_prime(7)


def test_10001st_prime():
    assert 104743 == nth_prime(10001)
