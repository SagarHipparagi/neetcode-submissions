# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest_diameter = 0
        
        def height(node):
            if not node:
                return 0
            
            # Recursively find the height of left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # The diameter at the current node is the sum of left and right heights
            current_diameter = left_height + right_height
            
            # Update the global maximum diameter found so far
            self.largest_diameter = max(self.largest_diameter, current_diameter)
            
            # Return the height of the current subtree to the parent call
            return 1 + max(left_height, right_height)
        
        height(root)
        return self.largest_diameter

        