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


def encoded_message_count(message):
    str_message = str(message)
    if str_message[0] == '0':
        return 'INVALID message'
    else :
        return message_count(str_message)


decode_message = []

def message_count(message):
    if len(message) == 1:
        count = 1
    elif len(message) == 2:
        if int(message) < 27 and int(message) > 0:
            count=2
        else:
            count=1
    else:
        count = message_count(message[1:])
        print(message[:2])
        if int(message[:2]) < 27 and int(message[:2]) > 0:
            count += message_count(message[2:])

    return count


if __name__ == '__main__':
    print(encoded_message_count(145))

