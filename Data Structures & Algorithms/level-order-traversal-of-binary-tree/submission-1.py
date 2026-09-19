# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        level = 1
        
        def traversalList(node, level = 0):
            if not node:
                return 
            
            res[level].append(node.val)
    
            traversalList(node.left, level + 1)
            traversalList(node.right, level + 1)
            

        traversalList(root)
        return list(res.values())



        