# This problem was asked by Amazon.
#
# Given an integer k and a string s, find the length of the longest substring
# that contains at most k distinct characters.
#
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".


def subString(s, k):
    longestSubString = ''
    for i in range(len(s)):
        for l in range( i +1 , len(s) +1):
            if k == len((set(s[i:l]))) and len(longestSubString) < len(s[i:l]):
                longestSubString = s[i:l]
    return longestSubString



if __name__ == "__main__":
    print(subString("abcba", 2))