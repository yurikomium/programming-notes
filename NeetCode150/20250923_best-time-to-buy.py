"""
Brute Force

Time Complexity: O(n^2)
Space Complexity: O(1)

"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 # 取引しないという選択肢（利益=0）を許可している
        for i in range(len(prices)):
            # 先に買う日を固定
            buy = prices[i]
            for j in range(i + 1, len(prices)): # iより後ろしか確認しない
                sell  = prices[j]
                res = max(res, sell - buy)
        return 
        
"""
Two Pointers

Time Complexity: O(n) - 価格リストを一度走査するため
Space Complexity: O(1) - 追加の空間を使用しないため

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 ## lは最安の買う日のインデックス、rは売る日候補のインデックス
        maxP = 0 ## これまで見た“売る日”に対する最大利益

        while r < len(prices):
            if prices[l] < prices[r]: ## 最安 l で買って今日 r に売ったらいくら？
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1 
        return maxP