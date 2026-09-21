# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        def fun(node, res, ans):
            if node is None:
                return 
            res += str(node.val) # Also sum = sum * 10 + digit we can use 
            if node.left is None and node.right is None:
                ans.append(int(res))
                return
            else:
                fun(node.left, res, ans)
                fun(node.right, res, ans)
        ans = []
        fun(root, "", ans)
        return sum(ans)
        
