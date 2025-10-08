"""
Iteration

Time Complexity: O(n) - リストの長さを n とすると、各ノードを一度ずつ処理するため
Space Complexity: O(1) - 追加のメモリをほとんど使用しないため

"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ## prev … すでに反転済みリストの先頭を指す（右向きに伸びていく）
        ## curr … 未処理のリストの「先頭」を指す（curr から先は元の向きのまま）
        prev, curr = None, head

        while curr:
            temp = curr.next ## curr.nextを書き換える前に、現状のnext以降を退避しておく
            curr.next = prev ## 矢印を反転
            prev = curr ## 反転済みリストの先頭はcurrに更新
            curr = temp ## 退避しておいた元のnextに進む
        return prev