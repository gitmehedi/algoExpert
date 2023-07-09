array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]


def isValidSubsequence(array, sequence):
    seq = 0
    for val in range(len(array)):
        if array[val] == sequence[seq]:
            seq += 1
        if seq == len(sequence):
            return True
    return False


print(isValidSubsequence(array, sequence))


def isValidSubsequence(array, sequence):
    for val in sequence:
        if val in array:
            array = array[array.index(val) + 1:]
        else:
            return False
    return True


print(isValidSubsequence(array, sequence))


def isValidSubsequence(array, sequence):
    arrInd = 0
    seqInd = 0

    while arrInd < len(array) and seqInd < len(sequence):
        if array[arrInd] == sequence[seqInd]:
            seqInd += 1
        arrInd += 1
    return seqInd == len(sequence)


print(isValidSubsequence(array, sequence))
