# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

def max_profit(prices:list[int])->int:
    # O(n^2) time and O(1) space
    max_profit = 0 
    for i in range(len(prices)):
        for j in range(i):
            if max_profit < prices[i] - prices[j]:
                max_profit = prices[i] - prices[j]
    return max_profit


def max_profit(prices:list[int]) -> int:
    max_profit = 0
    cheapest_price = float('inf')

    for i in range(len(prices)):
        if cheapest_price > prices[i]:
            cheapest_price = prices[i]
        
        max_profit = max(max_profit, prices[i] - cheapest_price)

        # if max_profit < prices[i] - cheapest_price:
        #     max_profit = prices[i] - cheapest_price
    return max_profit

print(max_profit([7,1,5,3,6,4]))

print(max_profit([7,2,5,3,4]))

print(max_profit([7,6,4,3,1]))

# Approach
# Create max profit variable and set to zero, create cheapest price variable and set to infinity
# Loop through prices 
#    if prices at current index is less than cheapest prices, cheapest price equals price at current index
#    if prices at current index - cheapest buy price is greater than max profit, then max profit equals that (meaning higher max profit for selling then)
# return max profit