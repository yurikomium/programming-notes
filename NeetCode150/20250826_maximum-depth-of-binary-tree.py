class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ## 葉ノードの場合1を返す
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))