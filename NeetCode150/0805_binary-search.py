## 再帰的二分探索

class Solution:
    def binary_search(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        ## オーバーフロー対策
        ### CやC++, Javaでは、l + rだと言語の整数の最大値を超える可能性がある ＝ オーバーフロー
        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        if nums[m] < target:
            ## ターゲットがmの右側にある場合
            return self.binary_search(m + 1, r, nums, target)
        ## ターゲットがmの左側にある場合
        return self.binary_search(l, m - 1, nums, target)

    ## シンプルなインターフェースを提供するためのメソッド
    ### 利用者はlとrを考える必要がないことが、この設計の利点
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)

### 計算量
# - 時間計算量：O(log n)
#   - n = 8の配列で何回比較するか数える
#     - 最大4回 ≈ log₂(8) + 1
# - 空間計算量：O(log n)
#   - 再帰のスタックを数える
#     - 最大3単位 ≈ log₂(8)