from itertools import combinations_with_replacement
from sequences.text import isPalindrome

# generate all the integers that when written are digits in length
def integers_of_length(digits):
    for n in range(10**(digits - 1), 10**digits):
        yield n


def n_by_n_palindromes(digits):
    """Return all integers that are products of two n-digit integers

    Parameters
    ----------
    digits : int
        number of digits in operands
    Returns
    -------
        products which pass the palindromic test
    """
    products = map(lambda t: t[0] * t[1],
                   combinations_with_replacement(integers_of_length(digits), 2))
    return filter(isPalindrome, products)
