# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

alphabets = {
    1:"a",
    2:"b",
    3:"c",
    4:"d",
    5:"e",
    6:"f",
    7:"g",
    8:"h",
    9:"i",
    10:"j",
    11:"k",
    12:"l",
    13:"m",
    14:"n",
    15:"o",
    16:"p",
    17:"q",
    18:"r",
    19:"s",
    20:"t",
    21:"u",
    22:"v",
    23:"w",
    24:"x",
    25:"y",
    26:"z"
}

allMessages = []

def decode(parsed, remaining):
    if remaining == "":
        if parsed not in allMessages:
            allMessages.append(''.join(parsed))
        else:
            print(parsed)
        return

    singleDigit = int(remaining[0])
    if singleDigit in range(1,27):
        decode(parsed+[alphabets[singleDigit]], remaining[1:])

    if len(remaining)>1:
        twoDigits = int(remaining[0:2])
        if twoDigits in range(1,27):
            decode(parsed+[alphabets[twoDigits]], remaining[2:])

if __name__ == "__main__":
    message = '2621'
    decode([], message)
    print(allMessages)
    print(len(allMessages))