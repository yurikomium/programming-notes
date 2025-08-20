# Binary Search

**Date:** 2025-08-18
**Platform:** NeetCode 150 https://neetcode.io/problems/invert-a-binary-tree?list=neetcode150
**Difficulty:** Easy

## Problem Description

Binary Tree を Invert（反転）する

## Key Learnings

- 問題に対して、どのアルゴリズムが適切かを判断できる必要がある
  - Tree Inversion の場合は、深さ優先探索(Depth-First Search, DFS)でも幅優先探索(Breadth-First Search, BFS)でも、どちらでも解ける
- 探索方法
  - BFS:
    - **横（幅）**から順番に探索
    - キューを使用
    - First In, First Out
  - DFS:
    - 深くまで進んでから次の分岐を探索
    - スタック（または再帰）を使用
    - LIFO（Last In, First Out）

## Memo

-
