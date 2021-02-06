"""
Prime Factoring problem #3

  The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import factoring.factor as factor


if __name__ == '__main__':
    print(max(factor.factor(600851475143)))
