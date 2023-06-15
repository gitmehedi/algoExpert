"""
URL: https://www.algoexpert.io/questions/run-length-encoding

"""

def runLengthEncoding(string):
    encodeArr, count, i = [], 0, 0

    while i < len(string) - 1:
        if string[i] == string[i + 1] and count < 9:
            count += 1
        else:
            encodeArr.append(str(count) + string[i])
            count = 1
        i = i + 1
    encodeArr.append(str(count) + string[i])

    return "".join(encodeArr)