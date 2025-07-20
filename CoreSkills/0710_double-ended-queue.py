# Doubly Linked List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None # 双方向リンク

# Linked List implementation of Double Ended Queue
class Deque:
    def __init__(self):
        # Create two dummy nodes and link them
        self.head = Node(-1)
        self.tail = Node(-1) # tailもダミーノードの扱い。実際のデータノードはheadとtailの間に挿入される
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail # ダミーノードの間にデータがないかを確認

    def append(self, value) -> None:
        new_node = Node(value)
        last_node = self.tail.prev
        # dequeでは新しいノードを追加するとき、nextとprevをつなぎ直す必要がある
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node # ★忘れない

    def appendleft(self, value) -> None:
        new_node = Node(value)
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        # 削除するノードを特定
        last_node = self.tail.prev
        # 返すべきデータを先に保存（nodeとしては削除されるが、値は返す必要がある）
        ## nodeとvalueは分けて考える！！
        value = last_node.value
        # ノードを削除
        prev_node = last_node.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        # 削除後でも値を返せる
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.value
        next_node = first_node.next

        self.head.next = next_node
        next_node.prev = self.head

        return value
