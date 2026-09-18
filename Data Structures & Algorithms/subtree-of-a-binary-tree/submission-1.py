# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.findSubtree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        
    def findSubtree(self, node, subnode):
        if not subnode and not node:
            return True
        if subnode and node and subnode.val == node.val:
             return (self.findSubtree(node.left, subnode.left) and
                    self.findSubtree(node.right, subnode.right))
        return False




        