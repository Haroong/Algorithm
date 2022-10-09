def maxProfit(prices):
    min_price, profit = prices[0], 0

    # get maximum profit gap
    for i in range(1, len(prices)):
        min_price = min(min_price, prices[i])
        profit = max(profit, prices[i] - min_price)

    return profit
