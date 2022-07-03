# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        level = [root]
        res = [root.val]
        while level:
            tmp = []
            for l in level:
                if l.left:
                    tmp.append(l.left)
                if l.right:
                    tmp.append(l.right)
            if tmp:      
                res.append(tmp[-1].val)
            level = tmp
                
        return res
                