"""
Depth First Search
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # [0] = balanced(T/F), [1] = height
            # 現在のノードにおける高さ差チェック
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 # 全てTrueのときのみTrueを返す
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]