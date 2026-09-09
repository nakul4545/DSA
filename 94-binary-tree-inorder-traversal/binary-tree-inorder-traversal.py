# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fun(node,res):
            if node is None: # root == None
                return 
            fun(node.left,res)
            res.append(node.val)
            fun(node.right,res)
            return
        res = []
        fun(root,res)
        return res