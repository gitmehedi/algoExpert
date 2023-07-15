"""
Linear Search
"""

list = [2, 3, 5, 12, 5, 6, 7, 8, 9]
target = 13


def linearSearch(list, target):
    for val in list:
        if val == target:
            return True
    return False


print(linearSearch(list, target))

"""
Merge Sorting
"""
array = [8, 5, 2, 9, 5, 6, 3]


def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    ans = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            ans.append(left[i])
            i += 1
        else:
            ans.append(right[j])
            j += 1
    remain = left[i:] + right[j:]
    ans.extend(remain)

    return ans


print(mergeSort(array))
