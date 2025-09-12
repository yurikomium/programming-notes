# Depth First Research

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val: # 前者がないと、pかqがNoneのときにAttributeErrorになる
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

"""
Time Complexity: O(n) - Nはノード数。全てのノードを一度ずつ訪問するため。各ノードでの処理はO(1)。
Space Complexity: O(h) - Hは木の高さ。再帰の深さは木の高さに依存。
    - Best Case: O(log n) - 平衡二分木の場合
    - Worst Case: O(n) - 片側に偏った木の場合
"""