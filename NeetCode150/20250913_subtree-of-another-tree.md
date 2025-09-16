# Binary Search

**Date:** 2025-09-13
**Platform:** NeetCode 150 https://neetcode.io/problems/subtree-of-a-binary-tree?list=neetcode150
**Difficulty:** Easy

## Problem Description

- 部分木が同じかどうかを判定する

## Key Learnings

1. root の各ノードを訪問して、そのノードを起点とした部分木が subRoot と同じかチェック
2. 2 つの木が同じかどうかの判定

## Memo

- Same Tree の問題と違い、「メインの木（root）の中で、subRoot と同じ構造の部分木を見つける」必要がある
- 空の木はどんな木でも、常に部分木として存在する
  - 「何も探していない」→「探す必要がない」→「条件は満たされている」→True
- 複雑な問題は、単純な問題に分割する（1 つの関数で全て対応する必要はない）
  - 探索+比較 -> 探索のみ, 比較のみ
