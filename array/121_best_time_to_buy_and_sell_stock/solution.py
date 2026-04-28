"""
121. Best time to but and sell stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
https://neetcode.io/problems/buy-and-sell-crypto/question

dynamic approach
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        low_price = prices[0]
        for i in range(len(prices)):

            if prices[i] < low_price:
                low_price = prices[i]
            
            if prices[i] - low_price > profit:
                profit = prices[i] - low_price
        
        return profit