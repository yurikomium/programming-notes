# Binary Search

**Date:** 2025-08-05
**Platform:** Core Skills https://neetcode.io/problems/binary-search?list=neetcode150
**Difficulty:** Easy

## Problem Description

Binary Search を実装する

## Key Learnings

- range の使い方
  - range が受け取れるのは「整数」のみ
    - 配列は受け取れずにエラーになる
- Binary Search の仕組み
  - 前提：sorted order である必要がある
  - 真ん中を見て、探索範囲を半分に絞る
    - 辞書のイメージ

## Memo

- 最初に思いついた方法は線形探索。これだと計算量が O(n)になる
- Facade（ファサード）パターン
  - 複雑な内部処理をまとめ、システムの外側にシンプルな API を提供するデザインパターンを指す。
  - クライアントはサブシステムの詳細を知らなくても、必要な機能を利用できる。
- 計算量
  - 時間計算量＝何回処理するか
  - 空間計算量＝どれだけメモリを使うか
