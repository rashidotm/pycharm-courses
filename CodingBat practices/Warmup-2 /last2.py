# Given a string, return the count of the number of times that a substring length 2
# appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1
# (we won't count the end substring).
#
#
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1
# last2('axxxaaxx') → 2


def last2(str):
    result = 0
    if len(str) <= 2:
        return result
    else:
        # last 2 chars, can be written as str[-2:]
        # last2 = str[len(str) - 2:]
        # sub = str[len(str)-2] + str[len(str)-1]
        sub = str[len(str)-2:]
        for x in range(len(str)):
            if x < len(str) - 2:
                compare = str[x] + str[x+1]
                if sub == compare:
                    result += 1
    return result


print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))
print(last2('xxx'))
print(last2('xx'))
print(last2(''))
print(last2('x'))
