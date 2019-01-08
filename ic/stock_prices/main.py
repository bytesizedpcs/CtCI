#! /usr/bin/python3

def get_max_profit(stock_prices):
    max_profit = 0

    for f_index, first_price in enumerate(stock_prices):
        for s_index, second_price in enumerate(stock_prices):

            if s_index > f_index and second_price > first_price:
                if second_price - first_price > max_profit:

                    max_profit = second_price - first_price

    print (max_profit)
    return max_profit

def greedy_max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = 0

    for current_price in stock_prices:
        min_price = min(min_price, current_price)

        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

    return max_profit

def perfect_max_profit(stock_prices):
    if len(stock_prices) < 2:
        raise ValueError('Stock prices need 2 prices')

    min_price = stock_prices[0]
    max_profit = stock_prices[1] - stock_prices[0]

    for index, current_price in enumerate(stock_prices):
        potential_profit = current_price - min_price

        max_profit = max(max_profit, potential_profit)

        min_price = min(min_price, current_price)

    return max_profit

stocks = [1, 10, 43, 2, 76, 33, 99, 2]
stocks2 = [10, 7, 5, 8, 11, 9]

get_max_profit(stocks)
get_max_profit(stocks2)
