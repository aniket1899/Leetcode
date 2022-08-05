# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # solution 1
#         node = head
#         visited = set()
#         while node:
#             if node in visited:
#                 return node
            
#             visited.add(node)
#             node = node.next
        
#         return False

        # solution 2:
        
        slow = head
        fast = head
        
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False
    
            