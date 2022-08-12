from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        
        nodes = deque([root])
        depth = 0
        while nodes:
            
            levlen = len(nodes)
            print(levlen)
            for _ in range(levlen):
                curr = nodes.popleft()
                if curr:
                    nodes.extend(curr.children)
            depth += 1
            
        return depth
            