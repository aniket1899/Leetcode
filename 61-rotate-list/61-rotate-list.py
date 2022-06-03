# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        i = 0
        N = 1
        
        prev = None
        node = head
        while node.next:
            prev = node
            node = node.next
            N+=1
            
        nodeLast = node
        node.next = head
        
        prev=node
        node=node.next
        
        print(node.val)
        k = k%N
        for i in range(0, N-k):
            prev=node
            node=node.next
            
        prev.next = None
        head = node
        
        return head