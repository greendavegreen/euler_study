from math import sqrt
from factoring.sieve import primes
import time
from typing import Iterable, AnyStr


def factor(x):
    return factor_using_prime_sequence(x, primes())


def factor_using_prime_sequence(x, candidates):
    residue = x
    factor_upper_bound = int(sqrt(x))
    f = next(candidates)
    while f <= factor_upper_bound:
        while residue % f == 0:
            residue = residue / f
            yield f
        f = next(candidates)

    if residue != 1:
        raise RuntimeError("residue is not one!")


def timed_factor(title: AnyStr, val: int, items: Iterable[int]):
    """Runs a timed factoring on a given prime generator

    Parameters
    ----------
    title : str
        name of this timing experiment
    val : int
        the integer to factor
    items :
        a prime number sequence generator 2,3,5,7,11,13,17...

    Returns
    -------

    """
    t = time.time()
    l = list(factor_using_prime_sequence(val, items))
    t2 = time.time()
    print(title)
    print('=' * len(title))
    print(t2 - t)
    print(l)
    print()


if __name__ == '__main__':
    target = 60085147514300
    timed_factor("Current", target, primes())

