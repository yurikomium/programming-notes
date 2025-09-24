"""
Brute Force

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell  = prices[j]
                res = max(res, sell - buy)
        return res