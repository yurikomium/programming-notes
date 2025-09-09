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
        # メイン関数はT/Fだけ欲しいが、計算には高さも必要なので、補助関数を実装する
        def dfs(root): # 返り値は[バランスが取れているか(T/F), 高さ]。ただし型は指定しなくてもいい。
            # 空ノードの処理を入れておかないと、NoneTypeのエラーになる
            if not root:
                return [True, 0] # 存在しないノードはバランスが取れているとみなすのでTrue

            left, right = dfs(root.left), dfs(root.right)
            # [0] = balanced(T/F), [1] = height
            # 現在のノードにおける高さ差チェック
            ## absは絶対値を求める
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 # 全てTrueのときのみTrueを返す
            # 一度Falseになったら、以降はずっとFalseを返す
            return [balanced, 1 + max(left[1], right[1])] # 現在のノードの分の高さを追加する

        return dfs(root)[0]

"""
Time Complexity: O(n) - Nはノード数。全てのノードを一度ずつ訪問するため。各ノードでの処理はO(1)。
Space Complexity: O(h) - Hは木の高さ。再帰呼び出しスタックの最大深さのため
"""