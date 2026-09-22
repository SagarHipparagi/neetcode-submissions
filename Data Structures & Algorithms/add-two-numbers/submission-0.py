# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0) # Dummy node to simplify building the new list
        curr = dummy
        carry = 0
        
        # Loop as long as there are nodes to process or a carry-over remains
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
                
            # Create a new node with the single-digit value
            curr.next = ListNode(carry % 10)
            curr = curr.next
            
            # Calculate the new carry for the next iteration
            carry //= 10
            
        return dummy.next

        