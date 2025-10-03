"""
Iteration


"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ## prev … すでに反転済みリストの先頭を指す（右向きに伸びていく）
        ## curr … まだ反転していない残りのリストの先頭を指す（curr から先は元の向きのまま）
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev