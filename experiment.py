"""

"""
prices = [7, 1, 5, 3, 6, 4]


def maxProfit(prices):
    buy = prices[0]
    sell = prices[0]
    profit = sell - buy
    for price in prices:
        if price < buy:
            buy = price
            sell = price
        if price > sell:
            sell = price
        if sell - buy > profit:
            profit = sell - buy

    return profit


print(maxProfit(prices))
