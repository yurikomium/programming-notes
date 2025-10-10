"""
Iteration

"""

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        ## ダミーノードを置く（結果リストの先頭）
        dummy = node = ListNode() ### 新しいノードを作成し、nodeとdummyが同じノードを指すようにする
        ### nodeは結果リストの現在の末尾（毎回動く）

        while list1 and list2:
            ## list1とlist2の先頭を比較し、小さいほうのnodeを結果リストに追加
            if list1.val < list2.val:
                node.next = list1 ### 末尾に接続
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2 ### どちらかがNoneになったらループ終了。残っているほうをそのまま接続

        return dummy.next