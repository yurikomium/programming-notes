# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # rootの中でsubRootと同じ部分木があるかどうか（探索）
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ## どんな木でも空の木は常に部分木に含まれる（何も探さなくていい）
        ### プログラムがクラッシュしないように追加しているエッジケース
        if not subRoot:
            return True
        ## 「探索対象（root）が空なのに、何かを探している」→見つからない→False
        if not root:
            return False
        ## rootの現在のノードから始まる部分木がsubRootと同じか？
        ### 各ノードでsameTreeチェック
        if self.sameTree(root, subRoot):
            return True
        ## rootの左部分木、右部分木にsubRootと同じ部分木があるか？
        ### ここで"subRoot"は変わらないのがポイント
        return (self.isSubtree(root.left, subRoot) or
               self.isSubtree(root.right, subRoot))

    # 2つの木が完全に同じ構造・値かを判定する（比較）
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        ## 子がないときはここに入る
        if not root and not subRoot:
            return True
        ## 値が同じなら、左の子同士・右の子同士も比較
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                   self.sameTree(root.right, subRoot.right))
        return False