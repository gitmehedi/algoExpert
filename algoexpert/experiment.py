"""
Bubble Sort
"""
list = [8, 5, 2, 9, 5, 6, 3]


def bubbleSort(list):
    arr = len(list)
    for i in range(arr):
        for j in range(arr - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


print(bubbleSort(list))

"""
Insertion Sort
"""
list = [8, 5, 2, 9, 5, 6, 3]


def insertionSort(list):
    arr = len(list)
    for i in range(1, arr):
        while list[i - 1] > list[i] and i > 0:
            list[i - 1], list[i] = list[i], list[i - 1]
            i -= 1
    return list


print(insertionSort(list))

"""
Selection Sort
"""
list = [8, 5, 2, 9, 5, 6, 3]


def selectionSort(list):
    arr = len(list)
    for i in range(arr):
        for j in range(i + 1, arr):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


print(selectionSort(list))

"""
mergeSort Sort
"""
list = [8, 5, 2, 9, 5, 6, 3]


def mergeSort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left = mergeSort(list[:mid])
    right = mergeSort(list[mid:])

    res = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    remain = left[i:] + right[j:]
    res.extend(remain)
    return res


print(mergeSort(list))

"""
quickSort Sort
"""
list = [8, 5, 2, 9, 5, 6, 3]


def quickSort(list):
    if len(list) < 2:
        return list

    pivot = list[0]
    less = [i for i in list[1:] if i < pivot]
    greater = [i for i in list[1:] if i >= pivot]
    return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort(list))
