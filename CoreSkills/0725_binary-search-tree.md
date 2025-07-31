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
- 再帰呼び出し
  - 呼び出し元の途中で再起呼び出しが行われ、戻ってきたらまたそこで処理を再開する。

```
1) removeHelper(curr=5, key=2) の中で──
   └─ 2 < 5 なので
      curr.left = removeHelper(curr=3, key=2)
         └─ 2 < 3 なので
            curr.left = removeHelper(curr=2, key=2)
               └─ curr.key == key かつ葉なので
                  return None
            ← ここで removeHelper(curr=2) が終わり、戻ってくる
         └─ 「戻ってきた None を curr.left にセット」 をやってから
            return curr（=3） を返す
      ← ここで removeHelper(curr=3) が終わり、戻ってくる
   └─ 「戻ってきた node 3 を curr.left にセット」 をやってから
      return curr（=5） を返す
← remove の呼び出し元に 5 を返し、self.root を更新
```

## Memo

- 初めての Medium、理解に時間がかかった。Easy だけ先に進めようかなと思ったが、アルゴリズムで Easy が少ないので、このままのやり方で進める。
