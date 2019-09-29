# This problem was asked by Amazon.
#
# Given a string, find the longest palindromic contiguous substring.
# If there are more than one with the maximum length, return any one.
#
# For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
# The longest palindromic substring of "bananas" is "anana".


def is_palindrome(str):
    return str == str[::-1]


def get_longest_palindrome_string(s):
    if not s or is_palindrome(s):
        return s

    s_front = get_longest_palindrome_string(s[1:])
    s_back = get_longest_palindrome_string(s[:-1])

    return s_front if len(s_front) >= len(s_back) else s_back

if __name__ == "__main__":
    print(get_longest_palindrome_string("bananas"))
