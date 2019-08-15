'''
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''


def checkSumPair(input, k):
    givenNumbers = set()
    for number in input:
        if (k - number) in givenNumbers:
            return True
        else:
            givenNumbers.add(number)
    return False


if __name__ == "__main__":
    input = [10, 15, 3, 7]
    k = 17
    print(checkSumPair(input, k))
