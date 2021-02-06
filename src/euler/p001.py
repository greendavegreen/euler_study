"""
Sum of multiples problem #1

  Find the sum of all the multiples of 3 or 5 below 1000

     example: sum_of_multiples([3,5],10) = sum(3,5,6,9)= 23
"""

import factoring.multiples as mult

if __name__ == '__main__':
    print(sum(mult.multiples([3, 5], 1000)))
