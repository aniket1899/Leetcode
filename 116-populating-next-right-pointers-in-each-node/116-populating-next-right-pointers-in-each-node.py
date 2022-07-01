"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        levelNodes = [root]
        
        while levelNodes:
            prev = levelNodes[0]
            # print(levelNodes)
            tmp = []
            if prev.left:
                tmp.append(prev.left)
                tmp.append(prev.right)
            level = None    
            for level in levelNodes[1:]:
                prev.next = level
                if level.left:
                    tmp.append(level.left)
                    tmp.append(level.right)
                prev = level
            prev = level or prev
            prev.next = None
            
            levelNodes = tmp
            
            
        return root
            
            
                