# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # if root is None:
        #     return False
        # def fun(node,res):
        #     if node is None:
        #         return 
        #     fun(node.left, res)
        #     res.append(node.val)
        #     fun(node.right, res)
        #     return 
        # res = []
        # fun(root, res)
        # # Now res is sorted because inorder sorts Now simply use two pointer approach 
        # i = 0 
        # j = len(res) - 1
        # while i<j:
        #     if res[i] + res[j] == k:
        #         return True
        #     elif res[i] + res[j] < k:
        #         i += 1
        #     else:
        #         j -= 1
        # return False

        # But the above approach is not optimal 
        stack = [root]
        seen = set()
        while stack:
            node = stack.pop()
            if k - node.val in seen:
                return True
            seen.add(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False 


        



