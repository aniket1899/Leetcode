# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if p is None and q is None:
            return True
        elif p and q:
            if p.val != q.val:
                return False
            else:
                pass
        else:
            return False
        
        levelP, levelQ = [p], [q]
        
        while levelP and levelQ:
            tmpP, tmpQ = [], []
            
            for nodeP, nodeQ in zip(levelP, levelQ):
                # left
                if nodeP.left is None and nodeQ.left is None:
                    pass
                elif nodeP.left and nodeQ.left:
                    if nodeP.left.val == nodeQ.left.val:
                        tmpP.append(nodeP.left)
                        tmpQ.append(nodeQ.left)
                    else:
                        return False
                else:
                    return False
                
                # right
                if nodeP.right is None and nodeQ.right is None:
                    pass
                elif nodeP.right and nodeQ.right:
                    if nodeP.right.val == nodeQ.right.val:
                        tmpP.append(nodeP.right)
                        tmpQ.append(nodeQ.right)
                    else:
                        return False
                else:
                    return False
            if len(levelP) != len(levelQ):
                return False
            levelP, levelQ = tmpP, tmpQ
        
        return True