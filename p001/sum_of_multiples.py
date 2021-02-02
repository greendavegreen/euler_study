"""Find the sum of all the multiples of 3 or 5 below 1000

sum_of_multiples([3,5],10) = sum(3,5,6,9)= 23

goal: sum_of_multiples([3,5],1000)

uses ints, range -2147483648 through 2147483647
"""
from itertools import chain
from operator import itemgetter
from typing import List, Iterable

from utils.sorted_collection import SortedCollection


def multiples_up_to(bases: List[int], limit: int) -> set:
    """Produces all multiples of each base of value less than limit."""
    return set(
        chain.from_iterable([range(base, limit, base)
                             for base in bases])
    )

# approach 2, explicitly test each base against each item in limit range


def mult_gen(mults: List[int], limit: int) -> Iterable:
    for n in range(1, limit):
        for d in mults:
            if n % d == 0:
                yield n
                break


# approach 3, blend ranges using knowledge of increasing order


def m_merge(bases: List[int], limit: int) -> Iterable:
    for base in bases:
        assert base < limit
    iterators = [iter(range(base, limit, base)) for base in bases]
    position = SortedCollection(zip([next(i) for i in iterators],
                                    range(len(iterators))),
                                key=itemgetter(0))

    last_yielded = 0

    while len(position) > 0:
        val, iter_index = position[0]
        if val > last_yielded:
            yield val
            last_yielded = val
        position.remove((val, iter_index))
        try:
            new_val = next(iterators[iter_index])
            position.insert((new_val, iter_index))
        except StopIteration:
            pass


if __name__ == '__main__':
    for _ in multiples_up_to([3, 5, 7], 10):
        pass
        # print(_)
