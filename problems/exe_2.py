# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of
# the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6]

import numpy as np
from functools import reduce

# using numpy
def arrayMultiplication(numbers):
    product = np.prod(numbers)
    return [product//i for i in numbers]

# by reduce
def arrayMultiplicationUsingResuce(numbers):
    product = reduce((lambda x,y:x*y), numbers)
    return [product//i for i in numbers]

if __name__ == "__main__":
    input = [1, 2, 3, 4, 5]
    print(arrayMultiplication(input))
    print(arrayMultiplicationUsingResuce(input))