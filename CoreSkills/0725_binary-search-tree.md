# 004 - Design Binary Search Tree

**Date:** 2025-07-25
**Platform:** Core Skills https://neetcode.io/problems/binarySearchTree
**Difficulty:** Easy

## Problem Description

Binary Tree を実装する

## Key Learnings

- Binary Tree: 辞書の一種。
  - 親子関係がある
    - 「左の子 < 親 < 右の子」と決められている
  - Root（＝トップノード）, Leaf Nodes
  - cycle を持たない, 同じ段の横はつながらない sibling nodes
  - Depth: root→children→children なら、Depth は 3
  - leaf node: 左右両方の子を持たないノード
- return の役割
  - return は早期終了。if 文だけでなく関数全体を終了する。
  - break は while ループを抜けるだけ。
- 部分木
  - 木の全体のうち、親子関係が保たれた一部分のこと。

## Memo

- 初めての Medium、理解に時間がかかった。Easy だけ先に進めようかなと思ったが、アルゴリズムで Easy が少ないので、このままのやり方で進める。
