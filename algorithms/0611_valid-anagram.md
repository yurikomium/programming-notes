# [Problem Number] - [Problem Name]

**Date:** 2025-06-11, 12, 13
**Platform:** NeetCode 150 https://neetcode.io/problems/is-anagram
**Difficulty:** Easy

## Problem Description

文字列がアナグラムかどうかの判定

## First Approach

最初に考えたアプローチ

- 時間計算量: O(n×m) = O(n) × O(m)
- 空間計算量: O(1) ← 変数 i のみを使用（定数空間）

```
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return False
        return True
```

## Optimized Solution

改善後のアプローチ

- 時間計算量: O(n) = O(1) + O(n) + O(k) ※k は最大で n
- 空間計算量: O(k)
- どこを改善したか: あらゆるパターンを網羅, ハッシュマップを使用

## Key Learnings

- "not in"の使い方 → 文字列に対して使う場合は線形探索なので O(m)
- 文字もソート可能
- ハッシュマップ: キーと値のペアを高速で格納・検索できるデータ構造
- get の使い方: Python の辞書（ハッシュマップ）のメソッドで、安全にキーの値を取得する。存在しないキーに対して None を返す。
- さまざまなパターンを想定し、不要な計算をしなくてすむように早めに終わらせる
- Counter は辞書の特殊版で、要素の出現回数を自動的に数える->Counter を使えば今回の問題は 1 行で終わる
  - Counter({'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1})
- sorted()は文字列を文字のリストに変換し、アルファベット順に並び替える。

## Mistakes Made

- anagram は、文字の個数も一致する必要がある
- return の位置: for 文の外に出さないと TF の結果が変わってしまう
