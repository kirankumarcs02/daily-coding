# This problem was asked by Amazon.
#
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time.
# Given N, write a function that returns the number of unique ways you can climb the staircase.
# The order of the steps matters.
#
# For example, if N is 4, then there are 5 unique ways:
#
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time,
# you could climb any number from a set of positive integers X? For example, i
# f X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.



def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum(staircase(n - x, X) for x in X)

def staircase_1(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
        print('cache = ',cache)
    return cache[n]

if __name__ == "__main__":
    print(staircase(4,[1,2]))
    print(staircase_1(4,[1,2]))

