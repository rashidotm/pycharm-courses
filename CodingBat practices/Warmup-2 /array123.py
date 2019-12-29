# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
#
#
# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True


def array123(nums):
    result = False
    length = len(nums)
    seq = [1, 2, 3]
    if length > 2:
        for x in range(length-2):
            if nums[x] == seq[0] and nums[x+1] == seq[1] and nums[x+2] == seq[2]:
                result = True
                break
    return result

print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
print(array123([1, 2, 3]))