# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if not root:
            return []
        def fun(node, remaining, ans,res):
            if node is None:
                return 
            remaining -= node.val
            res.append(node.val)
            if node.left is None and node.right is None:
                if remaining ==0:
                    ans.append(res.copy())
            else:
                fun(node.left, remaining, ans, res)
                fun(node.right, remaining, ans, res)
            res.pop()

        ans = []
        fun(root, targetSum, ans, [])
        return ans
