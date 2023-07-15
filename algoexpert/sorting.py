"""
Bubble Sorting
"""

array = [8, 5, 2, 9, 5, 6, 3]


def bubbleSort(array):
    arrlen = len(array)
    for i in range(arrlen):
        for j in range(arrlen - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


print(bubbleSort(array))

"""
Insertion Sorting
"""
array = [8, 5, 2, 9, 5, 6, 3]


def insertionSort(array):
    for x in range(1, len(array)):
        while array[x - 1] > array[x] and x > 0:
            array[x - 1], array[x] = array[x], array[x - 1]
            x -= 1
    return array


print(insertionSort(array))

"""
Selection Sorting
"""
array = [8, 5, 2, 9, 5, 6, 3]


def selectionSort(array):
    arrLen = len(array)
    for i in range(arrLen):
        for j in range(i + 1, arrLen):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

    return array


print(selectionSort(array))

"""
Quick Sorting
"""
array = [8, 5, 2, 9, 5, 6, 3]


def quickSort(array):
    if len(array) < 2:
        return array

    pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort(array))

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
