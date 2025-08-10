## 反復二分探索 ★★覚える★★
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r: # l > rになったら探索範囲が無効（存在しない範囲）
            # (l + r) // 2 can lead to overflow
            m = l + ((r - l) // 2)

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
        
### 計算量
# - 時間計算量：O(log n)
#   - n = 8の配列で何回比較するか数える
#     - 最大4回 ≈ log₂(8) + 1
# - 空間計算量：O(1)
#   - 変数l, r, mを数える
#     - 3単位


## 再帰的二分探索 ★★余力があれば差別化要因になる★★

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
#   - 再帰のスタック（再帰が何層に重なるか）を数える <- 再帰では前の関数が終了していないため
#     - 最大3単位 ≈ log₂(8)

## Upper Bound（上級問題レベル）
### 「targetと一致する要素を見つけること」ではなく、「targetより大きい最初の要素のインデックス（＝境界位置）を見つけること」が目的

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m
            elif nums[m] <= target:
                l = m + 1
        return l - 1 if (l and nums[l - 1] == target) else -1
        ## targetが見つかる場合は l - 1
        ## targetが存在しない場合・targetが配列の最小値より小さい場合は -1
        ## l = 0 もしくは nums[l - 1] != target の場合は、if文の結果がFalse。それ以外はTrue

### 計算量
# - 時間計算量：O(log n)
#   - n = 8の配列で何回比較するか数える
#     - 最大4回 ≈ log₂(8) + 1a
# - 空間計算量：O(1)
#   - 変数l, r, mを数える
#     - 3単位
#   - 再帰を使わないため、スタックは使わない