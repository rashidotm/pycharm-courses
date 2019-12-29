one = 1
two = 2
three = 3

print("one is greater than two, two is greater than three. is this true or false?", one < two < three)  # This chained comparison means that the (one < two) and (two < three) comparisons are performed at the same time.
print(one < two > one)  # This chained comparison means that the (one < two) and (two < three) comparisons are performed at the same time.
is_greater = three > two
print(is_greater)

