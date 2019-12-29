# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
#
#
# first_half('WooHoo') → 'Woo'
# first_half('HelloThere') → 'Hello'
# first_half('abcdef') → 'abc'


def first_half(str):
    result = ""
    for x in range(len(str)):
        if x < len(str)/2:
            result += str[x]
        else:
            break
    return result

print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
print(first_half('ab'))
print(first_half(''))
print(first_half('a'))
