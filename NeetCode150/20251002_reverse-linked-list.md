# Linked List

**Date:** 2025-10-02
**Platform:** https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150
**Difficulty:** Easy

## Problem Description

- LinkedList のポインタを付け替えていく

## Key Learnings

- ノード同士のつなぎ目（next ポインタ）だけを付け替えて、データ本体は一切動かさない
  - 参照しか変更しないので、安定・高速。

## Memo

- このループは、つねに
  L1（prev） = これまで処理したノードの逆順リスト
  L2（curr） = まだ処理してない元の順リスト
  という 2 本のリストを持っていて、L2 の先頭を 1 個だけ抜き取り、L1 の先頭に差す―
