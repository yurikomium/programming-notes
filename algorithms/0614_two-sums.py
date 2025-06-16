"""
配列を1回だけ走査して、各要素について『ペアになる相手』がすでに見た要素の中にあるかチェックする
- 時間計算量: 
- 空間計算量: 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # ハッシュマップ
        
        for i, num in enumerate(nums):
            difference = target - num     # ペアになる相手
            
            if difference in seen:       # O(1)チェック
                return [seen[difference], i]
            
            seen[num] = i               # 現在の要素を保存