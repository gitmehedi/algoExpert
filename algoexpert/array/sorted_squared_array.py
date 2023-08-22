array = [-2, -1]

"""
First Solution
"""


def sortedSquaredArray(array):
    result = []
    for val in array:
        result.append(val * val)
    return sorted(result)


print(sortedSquaredArray(array))

"""
Second Solution
"""


def sortedSquaredArray(array):
    small = 0
    large = len(array) - 1
    res = []
    while len(res) != len(array):
        sm_val = array[small] ** 2
        lg_val = array[large] ** 2
        if lg_val > sm_val:
            res.append(lg_val)
            large -= 1
        else:
            res.append(sm_val)
            small += 1
    res.reverse()
    return res


print(sortedSquaredArray(array))

nums = [3, 2, 2, 3]
val = 3


def removeElement(nums, val):
    for k in range(len(nums)):
        if nums[k] == val:
            nums.pop(k)
    return nums


print(removeElement(nums, val))
