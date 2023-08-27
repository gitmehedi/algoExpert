"""

"""

citations = [0, 3, 6, 1, 5]


def hIndex(citations):
    citations.sort()
    length = len(citations)
    for i in range(length):
        if citations[i] >= length - i:
            return length - i
    return 0


print(hIndex(citations))
