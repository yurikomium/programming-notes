# Binary Search

**Date:** 2025-08-25
**Platform:** NeetCode 150 https://neetcode.io/problems/depth-of-binary-tree?list=neetcode150
**Difficulty:** Easy

## Problem Description

## Key Learnings

- 深さ優先探索
  - 一番深いところから値が確定する
  - 値は下から上に返し、上で計算完了する

## Memo

- 発想方法
  - もし問題の答えがわかっていたら、どういう式が必要かを逆算する
    - 例：もし左右の子の深度がわかっていたら、親も解ける
    - -> 同じ種類の小さな問題に分解できる
  - 「深度って結局何か？」を考える
    - 実際は「ノードからノードへの移動回数」
    - ルートから葉への移動の最大回数
