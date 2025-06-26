# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val #このノードの値
        self.next = next_node # "=None"はデフォルトを指す

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # Init the list with a 'dummy' node which makes 
        # removing a node from the beginning of list easier.
        self.head = ListNode(-1) # ダミーノードを使うことで、リストの先頭からの削除を簡単にする
        self.tail = self.head  # リストの末尾もダミーノードで初期化。最初は空のリストなので、headとtailは同じノードを指す
        ## 実際は混乱を招くので、プライベート化したり、外部からアクセスできないようにすることが多い

        """
        初期状態：
        head/tail → [ダミー(-1)] → None

        データ追加後：
        head → [ダミー(-1)] → [実データ1] → [実データ2] → None
                                ↑              ↑
                            実際の先頭         tail
        """
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1  # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:  # If list was empty before insertion
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next
        
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res