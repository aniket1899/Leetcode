# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        level = 0 
        levelNodes = [root]
        res = []
        while levelNodes:
            tmp = []
            vals = []
            for l in levelNodes:
                vals.append(l.val)
                if l.left:
                    tmp.append(l.left)
                if l.right:
                    tmp.append(l.right)
            if level%2:
                vals = reversed(vals)
            res.append(vals)
            level += 1
            levelNodes = tmp
        return res