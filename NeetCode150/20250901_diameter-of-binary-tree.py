# depth first research
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # カプセル化: `res`と`dfs`は`diameterOfBinaryTree`  のプライベートな要素として、外部から干渉されない。

        res = 0
        def dfs(root):
            nonlocal res ## 外側のresを使用する宣言
            ## nonlocal: 内側の関数から外側の関数の変数を変更するためのキーワード

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right) ## 最長パスの追跡

            return 1 + max(left, right) ## 高さの計算 -> 左右の高さの合計値が最長パスかどうかを確認するために使う

        dfs(root)
        return res