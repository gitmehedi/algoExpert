def twoNumberSumFirst(array, targetSum):
    arrLen = len(array)
    result = []
    for first in range(arrLen):
        for sec in range(first + 1, arrLen):
            val1 = array[first]
            val2 = array[sec]
            if (val1 + val2) == targetSum:
                result.append(val1)
                result.append(val2)
    return result


def twoNumberSumSecond(array, targetSum):
    storage = set(array)
    for val in array:
        remain = targetSum - val
        if remain in storage and val != remain:
            return [val, remain]
    return []


def twoNumberSumThird(array, targetSum):
    for val in array:
        target = targetSum - val
        if val != target and target in array:
            return [val, target]
    return []


array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSumFirst(array, targetSum))
print(twoNumberSumSecond(array, targetSum))
print(twoNumberSumThird(array, targetSum))
