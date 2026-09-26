# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Handle base cases
        if not head or k == 1:
            return head
        
        # Create a dummy node to track the head of the modified list safely
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # 1. Identify if a full group of k nodes exists
            kth = self.getKthNode(group_prev, k)
            if not kth:
                break
                
            group_next = kth.next
            
            # 2. Reverse the current group of k nodes
            # 'prev' starts at group_next so the new tail seamlessly links to the rest of the list
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # 3. Connect the previous group's tail to the new head of this reversed group
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp  # Move group_prev to the tail of the newly reversed group
            
        return dummy.next

    def getKthNode(self, curr: ListNode, k: int) -> Optional[ListNode]:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

        