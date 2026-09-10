# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fun(node, res):
            if node == None: 
                return # This return is for nodes which are none like left of 1 right of 2 and left/right of 3
            fun(node.left, res)
            fun(node.right, res)
            res.append(node.val)
            return # This return for nodes which are not none after exectuing all functions of them return 
        res = []
        fun(root, res)
        return res
