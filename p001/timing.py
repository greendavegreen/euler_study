import timeit
from p001.sum_of_multiples import multiples_of_any_range

print(timeit.timeit(lambda: multiples_of_any_range([3, 5], 10000000), number=1))
