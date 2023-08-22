"""
Get Repeated Substring
"""
string = "clementisacap"


def getRepeatedSubString(string):
    res = []
    length = len(string)

    # def isPalindrome(palin):
    #     left, right = 0, len(palin) - 1
    #     while left < right:
    #         if palin[left] != palin[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True
    #
    #
    largest = ''
    for row in range(length):
        for col in range(row + 1, length + 1):
            unique = string[row:col]
            lst = []
            for un in unique:
                if un not in lst:
                    lst.append(un)
                else:
                    break
            if len(unique) == len(lst) and len(largest) < len(lst):
                largest = unique

    return largest

    # res.append(string[row:col])

    # for row in range(length):
    #     for col in range(row + 1, length + 1):
    #         palin = string[row:col]
    #         # if isPalindrome(palin) and len(palin) > 1:
    #         #     res.append(palin)

    # left, right = 0, 0
    # while right <= len(string):
    #     res.append(string[left:right])
    #     right += 1
    #
    # left, right = 0, length - 1
    # while left < right:
    #     res.append(string[left:right])
    #     left += 1
    #
    # left, right = 0, length
    # while left < right:
    #     res.append(string[left:right])
    #     left += 1
    #     right -= 1

    return res


print(getRepeatedSubString(string))
