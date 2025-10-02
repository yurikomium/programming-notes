# Stack

**Date:** 2025-09-29
**Platform:** https://neetcode.io/problems/validate-parentheses?list=neetcode150
**Difficulty:** Easy

## Problem Description

- スタックの性質を活かして、順序と種類を同時に検証する
  - いま一番内側（＝最後に開けた）括弧は`stack[-1]`
  - 閉じ括弧が来たら必ずこのトップを閉じるので、入れ子の順序が正しくなる

## Key Learnings

- スタックの「最後に入れたものから先に処理」する性質は、入れ子や対応づけに活用できる

## Memo

- 直前の操作を打ち消す場合：エディタの Undo や、ブラウザの Back/Forward、BackSpace も同じ発想
- 辞書はハッシュテーブルなので、平均 O(1)で値を取り出せる
