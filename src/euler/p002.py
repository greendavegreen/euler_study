"""
Sum of even fibonaccis problem #2

  By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values
do not exceed four million, find the sum of the even-valued terms.

"""

from itertools import takewhile
from typing import Iterable

import sequences.fib as fib


def values_less_than(limit: int, iterator: Iterable) -> Iterable[int]:
    return takewhile(lambda x: x < limit, iterator)


if __name__ == '__main__':
    print(sum(values_less_than(4000000, fib.even_fib())))
