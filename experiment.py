"""

"""
ratings = [1, 0, 2]
ratings = [1, 2, 2]
ratings = [1, 3, 2, 2, 1]


def candy(ratings):
    rlen = len(ratings)
    candy = [1] * rlen
    for i in range(1, rlen):
        if ratings[i] > ratings[i - 1]:
            candy[i] = candy[i - 1] + 1

    for i in range(rlen - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candy[i] = max(candy[i], candy[i + 1] + 1)
    return sum(candy)


print(candy(ratings))
