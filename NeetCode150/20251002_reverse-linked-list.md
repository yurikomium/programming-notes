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
  という 2 本のリストを持っていて、L2 の先頭を 1 個だけ抜き取り、L1 の先頭に差す。これを毎周やっている。
- 一度つないだ（書き換えた）node.next は“メモリ上のノードの中身”なので、次のループでもそのまま残る。
  - 変わるのはあくまで変数 prev / curr が“どのノードを指しているか”だけ。
- 最後は"prev"を返す想定で、ゴールから逆算して考える
- 処理の流れ（例：input = [0, 1, 2, 3]
  1. temp = curr.next
     temp = 1 → 2 → 3 → None
  2. curr.next = prev
     0.next = None に付け替え（ここで 0 が反転後の末尾になる） ## 配線の書き換え
  3. prev = curr
     prev = 0 → None ## 先頭ポインタを移す（変数 prev はまだ古い先頭（P）を指したままのため）
  4. curr = temp
     curr = 1 → 2 → 3 → None
