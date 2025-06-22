# 001 - Design Dynamic Array

**Date:** 2025-06-18 -
**Platform:** Core Skills https://neetcode.io/problems/dynamicArray
**Difficulty:** Easy

## Problem Description

Dynamic Array を実装する

## Key Learnings

- メモリアドレス: コンピュータのメモリ（RAM）内で、データが格納されている場所を示す番号のこと
- Static Array と Dynamic Array の違い
  - Static Array: サイズがコンパイル時または宣言時に決まり、実行中に変更できない。メモリ効率が良い。
  - Dynamic Array: サイズが実行時に変更可能で、容量が足りなくなったら自動的に拡張。メモリオーバーヘッドも起こりうる。長期的には効率的。利便性と引き換えに、時々の性能低下とメモリオーバーヘッドを受け入れる。
- Capacity（容量）と Size（サイズ）の区別
  - Capacity: メモリ上で確保済みの領域のサイズ
  - Size: 実際に格納されている要素の数
- Constructor: クラスのオブジェクトを作成するときに自動的に呼び出される特別なメソッド
  - 特徴: 戻り値なし。
  - Python の場合は `def __init__`
- popback: 配列の末尾の要素を削除して取得する
- pushback: 配列の末尾に要素を追加する（Python だと`list.append()`）
- self: クラス内のメソッドでは、定義として第一引数でインスタンスを受け取ることを示すために"self"を指定する。呼び出し時は、どのインスタンスに対する操作なのかを自動判定するので、引数として設定する必要がない。

## Next Steps

-
