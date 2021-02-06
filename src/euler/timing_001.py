import timeit
import factoring.multiples as mult

limit = 1000000
spacer = """
"""


def handler(bases, limit):
    print(timeit.timeit(lambda: sum(1 for _ in mult.multiples(bases, limit)), number=1))
    print(timeit.timeit(lambda: sum(1 for _ in mult.unique_multiples2(bases, limit)), number=1))


handler([3, 5], limit)
print(spacer)
handler([2, 3, 5, 7, 9, 11, 13, 15, 17], limit)
print(spacer)
handler(range(2,100), limit)

