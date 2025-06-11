# [Problem Number] - [Problem Name]

**Date:**
**Platform:**
**Difficulty:**

## Problem Description

問題の概要を簡潔に

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

- 時間計算量: O(?)
- 空間計算量: O(?)
- どこを改善したか

## Key Learnings

- "not in"の使い方 → 文字列に対して使う場合は線形探索なので O(m)
- 文字もソート可能
- ハッシュマップ: キーと値のペアを高速で格納・検索できるデータ構造

## Mistakes Made

- anagram は、文字の個数も一致する必要がある
- return の位置: for 文の外に出さないと TF の結果が変わってしまう
