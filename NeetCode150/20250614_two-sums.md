# 003 - Two Sum

**Date:** 2025-06-14, 15, 16
**Platform:** NeetCode 150 https://neetcode.io/problems/two-integer-sum
**Difficulty:** Easy

## Problem Description

問題の概要を簡潔に

## First Approach

最初に考えたアプローチ

- 時間計算量: O(n^2)
- 空間計算量: O(1)
- なぜこの方法を選んだか: for 文を回す方法を思いついたから。
  → i != j を満たしていなかった
  → 条件を追加

## Optimized Solution

改善後のアプローチ

- 時間計算量: O(n)
- 空間計算量: O(n)
- どこを改善したか: ハッシュマップを使う, 与式を置き換える

## Key Learnings

- satisfy the condition: 条件を満たす
- 値だけを使いたい場合は"for i in nums"で、インデックスを使う場合は range と len()を使う
- 式を置き換える
  - `nums[i] + nums[j] == target`から`difference == target - nums`
- コンビネーションで考える場合は、for 文を最初から最後まで回すと重複が生じる
- enumerate: リストの各要素に自動で番号（インデックス）を振ってくれる関数

```
fruits = ['りんご', 'バナナ', 'みかん']

# enumerateが実際に作るものを見てみる
enum_obj = enumerate(fruits)
print("enumerateの中身:", list(enum_obj))
# 出力: [(0, 'りんご'), (1, 'バナナ'), (2, 'みかん')]
```

## Next Steps

- 一度"Core Skills"に戻り、基礎を固めてから"NeetCode 150"に移る
