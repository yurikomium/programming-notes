## Recursion
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 ## 空のときはreturnの段階で1を返せるよう、ここでは"return 0"にする（Noneではない）
        ## 葉ノードの場合1を返す
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) ## 再帰のときはselfをつけるのを忘れずに！

## Stack
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 木の全ノードを訪問しながら、各地点の深さを測り、最も深い地点を記録する
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]] ## [ノード, 深さ] のペアをスタックに格納
        res = 0

        while stack: # 訪問予定のノードがなくなったら終了
            node, depth = stack.pop()

            if node: ## Noneが入ってきた場合はスキップ
                res = max(res, depth)
                # 親ノードの深さ + 1 = 子ノードの深さ
                stack.append([node.left, depth + 1]) ## Noneの場合も[None, depth+1]は保存される
                stack.append([node.right, depth + 1])
        return res

## Stackを使う理由
# - 深さを求める問題なので、「深く潜ってから戻る」DFSが合っている