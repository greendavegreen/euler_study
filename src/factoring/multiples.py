"""Support for generating multiples.

Efficient algorithms for finding all multiples of multiple bases.
"""
from itertools import chain
from typing import List, Iterable


def _multiples_up_to(bases: List[int], limit: int) -> List[Iterable]:
    """ Returns list of multiples of any base in input list
    less than limit.
    """

    return [range(base, limit, base) for base in bases]


def _dedupe_iterables(iterables: List[Iterable]) -> Iterable:
    """Filters duplicate values from list of Iterables."""
    return set(chain.from_iterable(iterables))


def multiples(bases: List[int], limit: int) -> Iterable[int]:
    """Generates unique multiples of several bases in no particular order.

    Example: unique_multiples([3,6],10]) -> [9,3,6]

    Parameters
    ----------
    bases : list of int
            integers which produce multiples
    limit : int
            upper bound of all multiples returned
    Returns
    -------
    Iterable[int]
        collection of unique base-multiples less than limit.
    """
    return _dedupe_iterables(_multiples_up_to(bases, limit))


def unique_multiples2(bases: List[int], limit: int) -> Iterable:
    """Generates unique multiples of several bases in increasing order.

    Iterates over the range of the limit.
    Tests each value in order and maintain uniqueness loop break on first match.

    Parameters
    ----------
    bases : list of int
            integers which produce multiples
    limit : int
            upper bound of all multiples returned
    Returns
    -------
    Iterable[int]
        collection of unique base-multiples less than limit.
    """
    for n in range(1, limit):
        for d in bases:
            if n % d == 0:
                yield n
                break


if __name__ == '__main__':
    print(multiples([3, 5], 10))
