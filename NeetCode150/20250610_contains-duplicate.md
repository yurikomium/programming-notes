# 001 - Contains Duplicate

**Date:** 2025-06-10  
**Platform:** NeetCode 150 https://neetcode.io/problems/duplicate-integer?list=neetcode150
**Difficulty:** Easy

## Problem Description

配列に重複する要素があるかどうかを判定する

## First Approach

二重ループで全ての組み合わせをチェック

- 時間計算量: O(n^2)
- 空間計算量: O(1)

## Optimized Solution

HashSet を使用(set は Python におけるハッシュセット　　　)

- 時間計算量: O(n)
- 空間計算量: O(n)
- set の検索が O(1)だから高速化

## Key Learnings

- set の検索は O(1)、list の検索は O(n)
- 時間とメモリはトレードオフの関係
- 早期終了で効率向上

以下の方法だと常に全要素処理することになる

```
def hasDuplicate(self, nums):
    return len(nums) != len(set(nums))
```

- エッジケース: 空の配列、要素が 1 つだけ、全部同じ要素などでも機能するのか？

## Mistakes Made

- 最初 list で in 演算子を使ってしまった
- Big O 記法の理解が曖昧だった(time, space)
