# 001 - Contains Duplicate

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

- 時間計算量: O(?)
- 空間計算量: O(?)
- どこを改善したか: ハッシュマップ解法を使う

## Key Learnings

- satisfy the condition: 条件を満たす
- 値だけを使いたい場合は"for i in nums"で、インデックスを使う場合は range と len()を使う
- 式を置き換える
  - `nums[i] + nums[j] == target`から`difference == target - nums[i]`

## Mistakes Made

-
-

## Next Steps

-
