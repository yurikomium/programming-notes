# Binary Search

**Date:** 2025-08-18
**Platform:** NeetCode 150 https://neetcode.io/problems/invert-a-binary-tree?list=neetcode150
**Difficulty:** Easy

## Problem Description

Binary Tree を Invert（反転）する

## Key Learnings

- 問題に対して、どのアルゴリズムが適切かを判断できる必要がある
  - Tree Inversion の場合は、深さ優先探索(Depth-First Search, DFS)でも幅優先探索(Breadth-First Search, BFS)でも、どちらでも解ける
- 今回の問題

  - 要件
    - 全ノードの左右を入れ替える必要がある
    - 順序は関係ない（どのノードから処理しても OK）
    - 各ノード 1 回ずつ処理すれば十分
  - 解法選択

    - 今回は DFS でも BFS（キュー）でも問題ない

      ```
          4
         / \
        2   7
       / \ / \
      1  3 6  9

      どの順序で訪問する？
      ・DFS: 4→2→1→3→7→6→9 (深さ優先)
      ・BFS: 4→2→7→1→3→6→9 (幅優先)
      ```

  - キューのメリット
    - レベル順に処理するため、各段階での結果が確認しやすい
    - 処理順序が予測可能なので、デバッグがしやすい

- 探索方法
  - BFS:
    - **横（幅）**から順番に探索
    - キューを使用
      - 先に入れるものが先に出てくるデータ構造（ところてん方式）
      - FIFO を最も効率的に実現できる
      - deque（両端キュー）：双方向連結リストなので効率が良い
    - First In, First Out
      - キュー以外にリストでも実現可能（ただし非効率）
  - DFS:
    - 深くまで進んでから次の分岐を探索
    - スタック（または再帰）を使用
      - 後に入れたものが先に出てくるデータ構造
    - LIFO（Last In, First Out）

## Memo

- deque 実装の振り返り
  - すでに忘れていたので復習。ようやく Core Skills と NeetCode150 のつながりが見えてきた。
  - NeetCode（LeetCode）上では関数として中身を理解していなくても呼び出せてしまうので、その中身を理解するために Core Skills があるっぽい。
