from itertools import islice, takewhile


def fib():
    """Yields values of the fibbonacci sequence. 0, 1, 1, 2, 3, 5, 8..."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def even_fib():
    """Yields event values of the fibbonacci sequence. 0, 2, 8...

       Since: ODD + ODD -> EVEN
              ODD + EVEN -> ODD
              the start values of EVEN, ODD will generate
              EVEN ODD ODD EVEN ODD ODD EVEN

       Selecting every 3rd value will yield all the even fibbonacci numbers.
    """
    return islice(fib(), 0, None, 3)


if __name__ == '__main__':
    print(sum(takewhile(lambda x: x < 4000000, even_fib())))

