# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not", return the string unchanged.
#
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'


def not_string(str):
    if len(str) < 3:
        return "not " + str
    elif str[0].upper() == "N" and str[1].upper() == "O" and str[2].upper() == "T":
        return str
    else:
        return "not " + str

