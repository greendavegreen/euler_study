"""
Palindrom Products of length n problem #4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers:

    9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

from sequences.length import n_by_n_palindromes


if __name__ == '__main__':
    print(max(n_by_n_palindromes(3)))
