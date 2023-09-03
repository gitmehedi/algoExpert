s = 'ABCD'


def permutations(s):
    chars = list(s)
    p = [0] * len(s)

    res = []

    lower, upper = 1, 0
    while lower < len(s):
        print(lower, "---", p[lower])
        if p[lower] < lower:
            upper = (lower % 2) * p[lower]
            chars[lower], chars[upper] = chars[upper], chars[lower]
            res.append("".join(chars))
            p[lower] += 1
            lower = 1
        else:
            p[lower] = 0
            lower += 1
    return res


print(permutations(s))
