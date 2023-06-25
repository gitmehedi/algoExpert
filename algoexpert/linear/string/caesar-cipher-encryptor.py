"""
URL: https://www.algoexpert.io/questions/caesar-cipher-encryptor
"""

"""
Solution 1: 
"""


def solution1(string, key):
    cipher = []
    newKey = key % 26
    for val in string:
        cipher.append(getNewLetterKey(val, newKey))

    return ''.join(cipher)


def getNewLetterKey(letter, key):
    newLetter = ord(letter) + key
    return chr(newLetter) if newLetter < 122 else chr(96 + newLetter % 122)


"""
Solution 2: 
"""


def solution2(string, key):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    cipher = []
    for val in string:
        order = (lower.index(val) + key) % len(lower)
        cipher.append(lower[order])

    return ''.join(cipher)


"""
===================================
"""
case1 = 'abc'
key = 2
response1 = solution1(case1, key)
response2 = solution2(case1, key)
print(response1)
print(response2)
