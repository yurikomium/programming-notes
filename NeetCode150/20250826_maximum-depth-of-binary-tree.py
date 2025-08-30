class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 ## 空のときはreturnの段階で1を返せるよう、ここでは"return 0"にする（Noneではない）
        ## 葉ノードの場合1を返す
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) ## 再帰のときはselfをつけるのを忘れずに！