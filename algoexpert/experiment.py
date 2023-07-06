def sumA(input):
    prev = ''
    sam = 1
    final = []
    for val in input:
        if prev == val:
            sam +=1
        else:
            if sam>3:
                sam=3
            else:
                sam=1
            final = final + list(sam * prev)
        prev = val
    final.append(val)

    return ''.join(final)


input = 'tuuuuuuriiiiiing'
print(sumA(input))
