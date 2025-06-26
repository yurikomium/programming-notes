# 002 - Design LinkedList

**Date:** 2025-06-26
**Platform:** Core Skills https://neetcode.io/problems/singlyLinkedList
**Difficulty:** Easy

## Problem Description

Linked List を実装する

## Key Learnings

- Linked List: 要素を順序づけて格納する。配列とは異なり、メモリ上では連続して配置されない。ListNode というオブジェクトで構成される。
  - ListNode
    - value: ノードの値
    - next: 次のノードへの参照
      - 最後のノードの next は null を指す。
- 基本操作
  - Traversal: while 文で先頭から末尾まで順にアクセス -> O(n)
  - Insertion: 目的のノードに直接アクセスできれば O(1)
  - Deletion: 目的のノードに直接アクセスできれば O(1)
