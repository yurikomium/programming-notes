# Singly Linked List Node
class ListNode:
    def __init__(self, val, next_node=None): ## ★ここは代入なので=を使う★
        self.val = val #このノードの値。ここで定義することで、ListNodeクラスのインスタンスはvalueを持つことができる
        self.next = next_node # "=None"はデフォルトを指す
        # 同じ変数名を使う必要があるので、間違えないように注意★

# Implementation for Singly Linked List
class LinkedList:
    def __init__(self):
        # 後続の問題を考慮して、今回はheadとtailを明示的に持つ設計にしている
        self.head = ListNode(-1) # 値が-1のListNodeを1つ作成。ダミーノードを使うことで、リストの先頭からの削除を簡単にする。ダミーの-1はただの目印。
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
    
    def get(self, index: int) -> int: # 連結リストにはインデックスで直接アクセスできないので、順番にたどる必要がある
        curr = self.head.next # ★★実際のデータの先頭。self.headにするとダミーノードが実際のデータとして扱われてしまう
        i = 0 # 現在のインデックス = 今何番目にいるかという「順序情報」。（headは-1なので、実際のデータは0から始まる）
        while curr: # currがNoneになるまで（リストの末尾に到達するまで）ループを続ける
            if i == index: # 数字と数字（indexとi）を比較する。currはノードオブジェクトなので型が違うと比較できない
                return curr.val # ListNodeクラスで定義されているので、curr.valで値を取得できる
            i += 1
            curr = curr.next
        return -1  # Index out of bounds or list is empty

    def insertHead(self, val: int) -> None: # リストの先頭に新しいノードを挿入
        new_node = ListNode(val) # 新しいノードを1つ作成（nextはデフォルトでNone）
        new_node.next = self.head.next # 新しいノードのnextを現在の先頭に設定
        """
        Before:
        new_node: [10] → None
        head(ダミー) → [20] → [30] → None

        After:
        new_node: [10] → [20] → [30] → None  ★ [20]につながれば、その後のノードも自動的に繋がる
                        ↗
        head(ダミー) → [20] → [30] → None
        """
        self.head.next = new_node #headから new_node への参照をつくる。ここでself.head.nextにNoneが入っている可能性がある。
        """
        ダミーから始まるリストには、[10]がまだ含まれていない。
        [10]を先頭にしたいのに、ダミーはまだ[20]を指している状態。

        After:
        head(ダミー) → [10] → [20] → [30] → None
                        ↑
                    new_node
        これでダミーのノードのnextとnew_nodeのnextが同じ[10]を指すようになった。
        """
        if not new_node.next:  # 追加したノードが唯一のデータ(=nextがNone)なら、それをtailにする。これがないとリストの構造が壊れる ★忘れがち★★
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val) # 元々Noneだったtailのnextに新しいノードを追加
        self.tail = self.tail.next # 更新しないと次の挿入時に間違った場所に挿入される

    def remove(self, index: int) -> bool:  # ★間違い多し★
        i = 0
        curr = self.head
        # index回だけループして、削除したい要素の1つ手前のノードまでcurrを移動
        ## なぜならSingly Linked List）では前のノードへの参照がなく、削除したいノードの1つ手前にcurrを配置する必要があるから
        while i < index and curr: ## currがNoneになっていないかを確認→なっているとエラーになるため★★
            i += 1
            curr = curr.next 
        """ 
        Before:
        [1] -> [2] -> [3] -> [4] -> None
                ↑      ↑      ↑
              curr curr.next curr.next.next
        """
        
        # curr.nextが削除対象。currがすでに末尾の場合、curr.nextはNoneになるので、削除できない
        if curr and curr.next:
            if curr.next == self.tail: # 削除するノードがtailなら、tailを更新★★
                self.tail = curr ## 向きを間違えがち★★
            curr.next = curr.next.next # 削除するノードのnextを、削除するノードの次のノードに繋ぎ直す
            return True
        return False
        """
        After:
        [1] -> [2] -----> [4] -> None
                ↑          ↑
                curr      新しいcurr.next

                [3] <- このノードはもう誰からも参照されない（削除される）
        """

    def getValues(self) -> List[int]:
        curr = self.head.next # ダミーヘッドの次のノードから始める
        res = []
        while curr: # currがNoneになるまでループ
            res.append(curr.val)
            curr = curr.next
        return res