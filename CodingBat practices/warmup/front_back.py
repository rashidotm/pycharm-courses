# Given a string, return a new string where the first and last chars have been exchanged.
#
#
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

# CODINGBAT solution:

# #def front_back(str):
#   if len(str) <= 1:
#     return str
#
#   mid = str[1:len(str)-1]  # can be written as str[1:-1]
#
#   # last + mid + first
#   return str[len(str)-1] + mid + str[0]

def front_back(str):
    if len(str) == 0 or len(str) == 1:
        return str
    elif len(str) == 2:
        return str[1] + str[0]
    else:
        first_char = str[0]
        last_char = str[len(str)-1]
        return last_char + str[1:len(str)-1] + first_char

print(front_back("a"))
print(front_back(""))
print(front_back("ab"))
print(front_back("abc"))
print(front_back("abcdefg"))


