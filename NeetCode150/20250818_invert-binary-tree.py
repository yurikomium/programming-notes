# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left   # TreeNode または None
#         self.right = right   # TreeNode または None


## BFS（幅優先探索）を用いた二分木の反転
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # TreeNode型 または None
        if not root: ## 空の木が入力される場合を想定しておく
            return None
        queue = deque([root]) ## rootを唯一の要素として持つリストを、キュー（deque）に変換している
        while queue: # 両方の子がない場合はpopleftされるのみで、queueが空になるまで続ける
            node = queue.popleft() # LeetCodeでは自動でimportされる。queueからは左端の要素が失われる
            node.left, node.right = node.right, node.left # rootの左右の子ノードを入れ替える
            if node.left: # Noneだとエラーになるため、存在チェックを行う（子がない場合は通過）
                queue.append(node.left) # 処理できていない子ノードをキューに追加していく
            if node.right:
                queue.append(node.right)
            # left, rightどちらも存在する場合は両方をキューに追加する。
            ## 1回のループで1つのノードしか処理できない。自分の直接の子だけ入れ替える。
        return root # 中身は反転済みの木を返す

## 深さ優先探索（DFS）を用いた二分木の反転
### スタックを用いる -> 右の子から先に処理する

## 再帰的なアプローチによる二分木の反転
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root



メモ：再帰で書いてみる