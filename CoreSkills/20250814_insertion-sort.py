# Definition for a pair.
## 面接では定義が必要かを面接官に確認するとベター
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

## Pair型の定義により、複合データ型を扱える
# 2つの情報をセットで扱うことができるため、必須ではないが使いやすい。
# Pair: (5, "apple") - 一つのペア： (キー, 値) のセット
# 入力: List[Pair]
# [(5, "apple"), (2, "banana"), (9, "cherry")]
# 出力: List[List[Pair]]
# [
#  [(5, "apple"), (2, "banana"), (9, "cherry")],   # ステップ1
#  [(2, "banana"), (5, "apple"), (9, "cherry")],   # ステップ2
#  [(2, "banana"), (5, "apple"), (9, "cherry")]    # ステップ3
#]

class Solution:
    # Implementation of Insertion Sort
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []  # To store the intermediate states of the array
        
        for i in range(n):
            j = i - 1

            # Move elements that are greater than key one position ahead
            while j >= 0 and pairs[j].key > pairs[j + 1].key: ## iを使うと数字がズレるので、j + 1を使う点に注意。
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j] ## スワップ=交換処理。j + 1 = i
                j -= 1 ## より前の要素と比較するため
            
            # Clone and save the entire state of the array at this point
            res.append(pairs[:]) ## [:]はリストのコピーをつくる記号。本体ではなくコピーを保存。参照するとpairsが変わればresも変わるため。

        return res
