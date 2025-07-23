# 003 - Design Double-ended Queue

**Date:** 2025-07-10
**Platform:** Core Skills https://neetcode.io/problems/queue
**Difficulty:** Easy

## Problem Description

queue を実装する

## Key Learnings

- Queue
  - First In, First Out
  - 一方向のみ操作が可能
    - dequeue: キューの前から要素を取り出す（列の先頭から出る）
    - enqueue: キューの後ろに新しい要素を追加する（列に並ぶ）
- Deque（Double-ended Queue: 両端キュー）
  - 両端で要素の追加・削除が可能
    - そのために"prev"と"next"の両方への参照が必要

## Memo

- アルゴリズムの勉強を始めて 1 ヶ月、すごく成長は遅いけれど、Deque の問題を解くときに前回よりは理解できていることが多くて嬉しい！
- prev をつなぎ忘れがち。気をつける。
- 変数名には直感的な名前をつける
  - 直感的: last_node, first_node, prev_node, next_node など
