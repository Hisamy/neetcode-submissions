# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def countDepth(node):
            if not node:
                return -1
            left = 1 + countDepth(node.left)
            right = 1 + countDepth(node.right)
            return max(left, right)

        return 1 + countDepth(root)
        
        