"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        # Dictionary to map old nodes to their deep copies
        # None maps to None to safely handle null pointers
        old_to_new = {None: None}
        
        # First pass: Create all new nodes with matching values
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Second pass: Link the next and random pointers
        curr = head
        while curr:
            new_node = old_to_new[curr]
            new_node.next = old_to_new[curr.next]
            new_node.random = old_to_new[curr.random]
            curr = curr.next
            
        return old_to_new[head]

        