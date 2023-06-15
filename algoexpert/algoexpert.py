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

def runLengthEncoding(string):
    # Write your code here.
    encodeArr, count = [], 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1] and count < 9:
            count += 1
        else:
            encodeArr.append(str(count) + string[i])
            count = 1

    encodeArr.append(str(count) + string[-1])

    return "".join(encodeArr)


string = [
    'AAAAAAAAAAAAABBCCCCDD',
    'aA',
]

for st in string:
    res = runLengthEncoding(st)
    print(res)
