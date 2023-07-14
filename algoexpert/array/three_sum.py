array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0


def threeNumberSum(array, targetSum):
    res = []
    arrlen = len(array)
    for first in range(arrlen):
        for sec in range(first + 1, arrlen):
            next = targetSum - (array[first] + array[sec])
            if next in array:
                new_arr = [array[first], array[sec], next]
                res.append(new_arr)

    return res


print(threeNumberSum(array, targetSum))
