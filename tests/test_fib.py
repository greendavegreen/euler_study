import sequences.fib as fib
import itertools as it


def test_fib():
    assert list(it.islice( fib.fib(), 7)) == [0, 1, 1, 2, 3, 5, 8]


def test_even_fib():
    assert list(it.islice( fib.even_fib(), 3)) == [0, 2, 8]
