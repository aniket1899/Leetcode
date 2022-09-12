# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthHelper(self, node, n):
        if not node:
            return 1, node
        
        idx, curr = self.removeNthHelper(node.next, n)
        # print(idx, node)
        if idx == n + 1:
            if node.next:
                node.next = node.next.next
            else:
                node = None
        
        return idx+1, node
            
        
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        idx, node = self.removeNthHelper(head, n)
        if idx-1 == n:
            head = head.next
            
        return head
