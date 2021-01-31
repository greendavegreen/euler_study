"""Find the sum of all the multiples of 3 or 5 below 1000

sum_of_multiples([3,5],10) = sum(3,5,6,9)= 23

goal: sum_of_multiples([3,5],1000)

uses ints, range -2147483648 through 2147483647
"""



# approach one: use range iterables and sets to dedupe sequences of multiples

def multiples_of_any_range(bases, limit):
    result = set()
    for iterable in [range(base, limit, base) for base in bases]:
        result.update(iterable)
    return result


if __name__ == '__main__':
    print(sum(multiples_of_any_range([3, 5], 1000)))
