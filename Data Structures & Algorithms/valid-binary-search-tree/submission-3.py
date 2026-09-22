# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, limitLeft, limitRight):
            if not node:
                return True

            if not (limitLeft < node.val < limitRight):
                return False

            return (dfs(node.left, limitLeft, node.val) and
                    dfs(node.right, node.val, limitRight))
  
        return dfs(root, -1000000000, 1000000000)



        