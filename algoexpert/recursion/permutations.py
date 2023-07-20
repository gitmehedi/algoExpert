"""
Permutations
"""
ls = [1, 2, 3, 4, 6]


def permutations(ls):
    if len(ls) == 0:
        return []

    if len(ls) == 1:
        return [ls]

    res = []

    for i in range(len(ls)):
        m = ls[i]
        remain = ls[:i] + ls[i + 1:]
        for p in permutations(remain):
            res.append([m] + p)
    return res


print(permutations(ls))

"""
Permutations
"""
ls = [1, 2, 3]


def permutations(ls):
    res = []
    if len(ls) == 1:
        return [ls]
    else:
        for i in range(len(ls)):
            for p in permutations(ls[:i] + ls[i + 1:]):
                res.append([ls[i]] + p)

    return res


print(permutations(ls))
