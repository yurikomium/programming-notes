# 002 - Design LinkedList

**Date:** 2025-06-26
**Platform:** Core Skills https://neetcode.io/problems/singlyLinkedList
**Difficulty:** Easy

## Problem Description

Linked List を実装する

## Key Learnings

- Linked List: 要素を順序づけて格納する。配列とは異なり、メモリ上では連続して配置されない。ListNode というオブジェクトで構成される。
  - ListNode
    - node: 1 つの箱。連結リスト = 箱を矢印で繋げた列車
    - value: ノードの値
    - next: 次のノードへの参照
      - 最後のノードの next は null を指す。
- 基本操作
  - Traversal: while 文で先頭から末尾まで順にアクセス -> O(n)
  - Insertion: 目的のノードに直接アクセスできれば O(1)
  - Deletion: 目的のノードに直接アクセスできれば O(1)
- for と while
  - for: 長さがわかっているときに使う（繰り返し回数が事前にわかる）
  - while: 条件が満たされるまで繰り返す（終了条件が動的に決まる）
- tail と next
  - tail: 連結リスト全体の管理用の目印
  - next: 各ノードが「自分の次は誰か」を覚えている属性
- Python は、引数が nullable かを明記する必要がない（型ヒントも任意）
- 配列と LinkedList の違い
  - 連結リストには配列のような「直接アクセス」がない。インデックスで指定できず、順番にたどる必要がある。
- 参照系（どこを指すか）とデータ系（何の値か）の違い
  - head, tail, next, curr: 全てノードオブジェクトへの参照。「どのノードを指しているか」という位置情報を示す。値は ListNode オブジェクト。
  - val, index: 全て数値データ。「何の値を持っているか」という内容情報。値は int 型
