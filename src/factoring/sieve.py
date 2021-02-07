from math import sqrt
from itertools import cycle
from typing import Iterable


def primes() -> Iterable[int]:
    """yields prime integers in increasing order

    Tests successive candidates using array of primes found during search.

    Uses a 30 number cycle where every 2nd, 3rd, 5th item is skipped.
    This allows it to test only 8 out of each 30 integers.

    ie, in the range 1-30 it will test     1,  7,  11, 13, 17, 19, 23, 29
        in the range of 31-60 it will test 31, 37, 41, 43, 47, 49, 53, 59

    during this cycle, it has no need to test for divisibility by 2, 3, or 5.
    other primes up to the sqrt of a candidate being tested are considered

    Returns
    -------
    int
        next prime number
    """
    yield 2
    yield 3
    yield 5
    yield 7
    prime_list = [7]
    gap = cycle([2, 4, 2, 4, 6, 2, 6, 4])

    candidate = 11
    maximum_factor = 3

    while True:
        if maximum_factor * maximum_factor < candidate:
            maximum_factor += 1
        for p in prime_list:
            if p > maximum_factor:
                yield candidate
                prime_list.append(candidate)
                candidate += next(gap)
                break

            if candidate % p == 0:
                candidate += next(gap)
                break
