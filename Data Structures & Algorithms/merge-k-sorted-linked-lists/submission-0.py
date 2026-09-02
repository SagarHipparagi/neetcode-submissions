# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
from typing import List, Optional

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges K sorted linked lists into one sorted linked list using a Min-Heap.
        """
        min_heap = []
        
        # Step 1: Push the head of each non-empty linked list into the min-heap.
        # We include the index `i` as a tie-breaker to prevent Python from 
        # comparing ListNode instances directly if two nodes have the same value.
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(min_heap, (head.val, i, head))
        
        # Step 2: Initialize a dummy node to easily build the resulting list
        dummy = ListNode(0)
        current = dummy
        
        # Step 3: Continuously extract the minimum element and append it to our list
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            # Connect the smallest node to our merged list
            current.next = node
            current = current.next
            
            # If the extracted node has a next pointer, push the next node into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next
