from heapq import heapify, heappop, heappush

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        stack = [(head.val, id(head), head)  for head in lists if head]
        # print(stack)
        heapify(stack)
        
        if not len(stack):
            return None
        _,_, node = heappop(stack)
        
        if node.next:
            heappush(stack, (node.next.val,id(node.next), node.next))
            node.next = None
        sortedList = node
        sortedListHead = node
        while stack:
            _,_, node = heappop(stack)
            if node.next:
                # print(stack)
                # print(node.next.val, node.next)
                # print('--')
                heappush(stack, (node.next.val, id(node.next), node.next))
                node.next = None
            sortedList.next = node
            sortedList = sortedList.next
        return sortedListHead
        
                
            
                