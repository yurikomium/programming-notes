# Binary Search Tree Node
## keyは検索・比較・並び順の基準。一意である必要がある
## valueは実際に格納したいデータ。keyとvalueはペアで扱う。
class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

# Implementation for Binary Search Tree Map
class TreeMap:
    def __init__(self):
        ## この時点では木は空
        ## rootがわかればそこから全てのノードにアクセスできるため、rootだけを指定すればいい
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return # 早期終了のためのreturn。何も返さない。

        current = self.root
        while True: # 適切な挿入位置を見つけるまで木を辿り続ける操作。各分岐にreturnがあるため、無限ループにはならない
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else: # key==current.keyの場合
                current.val = val # 同じkeyが存在する場合は、値を上書きする（一意性の保持）
                return

    def get(self, key: int) -> int:
        current = self.root
        while current != None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return current.val
        return -1

    def getMin(self) -> int:
        current = self.findMin(self.root)
        return current.val if current else -1 # 三項演算子。currentが存在する場合はその値を、存在しない場合は-1を返す

    # Returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode: # 値だけでなくノード全体が必要。classは返り値の型としても使用できる
        while node and node.left:
            node = node.left
        return node

    def getMax(self) -> int:
        current = self.root
        while current and current.right:
            current = current.right
        return current.val if current else -1
    
    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Returns the new root of the subtree after removing the key
    ## 削除処理後の部分木の新しいルートノードを返す
    ### 入力: curr（部分木の根）と key
    ### 出力: key を削除したあとの「新しい部分木の根」
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None: # 1）この部分木に削除対象のNodeが存在しない場合
            return None

        if key > curr.key:  # 2) 探している key が大きければ右部分木へ
            ## 子が1つ以下のノードは、その子（あるいはNone）を返すだけで削除完了
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key: # 3) 探している key が小さければ左部分木へ
            curr.left = self.removeHelper(curr.left, key)
        else: # 4) curr.key == key → 削除対象を発見！
            if curr.left == None: 
                ## 葉ノード（左右の子がないノード）の場合はこの条件に入る
                # 4-1) 左が無ければ、右部分木と置き換え
                return curr.right
            elif curr.right == None:
                # 4-2) 右が無ければ、左部分木と置き換え
                return curr.left
            else: # 削除対象のノードが、左右両方の子を持つ場合
                # 4-3) 左右両方の子あり → inorder successor（右部分木の最小）と入れ替え
                minNode = self.findMin(curr.right) ## 1.ノードの右部分木から最小のノードを見つける
                curr.key = minNode.key　## 2.削除対象のノードのkeyを、見つけた最小ノードのkeyに置き換える
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key) ## 3.見つけた最小ノードを削除するために、再帰的にremoveHelperを呼び出す
                ## minNodeは右部分木の最小値なので、左の子を持たない
        # 5) 再帰から戻ってきた部分木の根を返す
        return curr # ★重要★

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root != None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)