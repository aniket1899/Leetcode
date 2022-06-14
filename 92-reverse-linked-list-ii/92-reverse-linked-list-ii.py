# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
#     def reverse(self, prev, node, left, right, depth):
#         if depth == right or not node.next:
#             return node
        
#         elif depth > left 
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
         
        node= head 
        prev = None
        leftnode = None
        rightnode = None
        length = 1
        while length <= right:
            if length > left:
                tmp = node.next
                node.next = prev
                prev = node
                node = tmp
            elif length == left:
                start = node
                leftnode = prev
                prev = node
                node = node.next
            else:
                prev = node
                node = node.next
                
            length += 1
            
        print(start.val, prev.val)
        if leftnode:
            leftnode.next = prev
            
        else:
            head = prev
        
        start.next = node
        
        return head
            
                