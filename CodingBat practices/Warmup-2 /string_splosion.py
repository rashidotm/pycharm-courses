# Given a non-empty string like "Code" return a string like "CCoCodCode".
#
#
# string_splosion('Code') → 'CCoCodCode'
# string_splosion('abc') → 'aababc'
# string_splosion('ab') → 'aab'


def string_splosion(str):
    result = ""
    for x1 in range(len(str)):
        for x2 in range(len(str)):
            if x2 <= x1:
                result += str[x2]
    return result


print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
print(string_splosion(''))
print(string_splosion('a'))