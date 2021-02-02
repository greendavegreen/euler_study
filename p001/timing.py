import timeit
from p001.sum_of_multiples import multiples_up_to, mult_gen, m_merge

limit = 10000000
spacer = """
"""


def test(bases, limit):
    print(timeit.timeit(lambda: sum(1 for _ in multiples_up_to(bases, limit)), number=1))
    print(timeit.timeit(lambda: sum(1 for _ in mult_gen(bases, limit)), number=1))
    print(timeit.timeit(lambda: sum(1 for _ in m_merge(bases, limit)), number=1))


test([3, 5], limit)
print(spacer)
test([2, 3, 5, 7, 9, 11, 13, 15, 17], limit)
print(spacer)
test(range(2,100), limit)

