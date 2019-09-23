# This problem was asked by Google.
#
# Given an array of integers where every integer occurs three
# times except for one integer, which only occurs once,
# find and return the non-duplicated integer.
#
# For example, given [6, 1, 3, 3, 3, 6, 6],
# return 1. Given [13, 19, 13, 13], return 19.


def get_non_duplicate(arr):
    non_duplicate = 0
    number_count = dict()
    for i in arr:
        if i in number_count:
            number_count[i] +=1
        else:
            number_count[i] = 1

    for key in number_count.keys():
        if number_count[key] == 1:
            non_duplicate = key

    return non_duplicate


if __name__ == "__main__":
    print(get_non_duplicate([13, 19, 13, 13]))