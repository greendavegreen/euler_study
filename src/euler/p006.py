"""Sum of squares  problem #6

The sum of the squares of the first ten natural numbers is,

sum of the squares is
385

the square of the sums is
3025

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.

"""


def square(x):
    return x * x


def sum_of_squares(items):
    return sum(map(square, items))


def square_of_sums(items):
    return square(sum(items))


def square_diff(items):
    return square_of_sums(items) - sum_of_squares(items)


if __name__ == '__main__':
    print(square_diff(range(1,101)))
