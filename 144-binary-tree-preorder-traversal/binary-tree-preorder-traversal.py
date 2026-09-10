# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Pre order means node -> left -> right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def fun(node, res):
            if node == None:
                return 
            res.append(node.val)
            fun(node.left, res)
            fun(node.right, res)
            return
        res= []
        fun(root, res)
        return res