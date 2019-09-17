def is_palindrome(s):
    return s[::-1] == s


def get_nearest_palindrome(s):

    if is_palindrome(s):
        return s

    if s[0] == s[-1]:
        return s[0] + get_nearest_palindrome(s[1:-1]) + s[-1]
    else:
        pal_1 = s[0] + get_nearest_palindrome(s[1:]) + s[0]
        pal_2 = s[-1] + get_nearest_palindrome(s[:-1]) + s[-1]

        if len(pal_1) > len(pal_2):
            return pal_2
        elif len(pal_1) < len(pal_2):
            return pal_1
        return pal_1 if pal_1 < pal_2 else pal_2


print(get_nearest_palindrome("racecar"))
print(get_nearest_palindrome("google"))
