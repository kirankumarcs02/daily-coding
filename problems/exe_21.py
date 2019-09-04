# This problem was asked by Snapchat.
#
# Given an array of time intervals (start, end) for classroom lectures
# (possibly overlapping), find the minimum number of rooms required.
#
# For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


def possible_overlapping(intervals):
    global_start_time = [start for start, end in intervals]
    global_end_time = [end for start, end in intervals]
    overlapping_count = 0
    for (start, end), i in zip(intervals, range(len(intervals)-1)):
        for j in range(i, len(intervals) - 1):
            start_count = False
            end_count = False
            if global_start_time[j + 1] <= start and end >= global_end_time[j + 1]:
                start_count = True
            if global_start_time[j + 1] >= end and end <= global_end_time[j + 1]:
                end_count = True
            if start_count or end_count:
                overlapping_count += 1
    return overlapping_count


if __name__ == "__main__":
    print(possible_overlapping([(30, 75), (0, 50), (60, 150)]))