# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize global maximum to negative infinity to handle all-negative trees
        self.max_sum = float('-inf')
        
        def get_max_gain(node):
            if not node:
                return 0
            
            # Recursively find the max gain from left and right subtrees
            # If a subtree returns a negative sum, ignore it by clamping to 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Price of the path if the current node acts as the highest pivot point (split)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum found so far
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum single branch sum back up to the parent node
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return self.max_sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize global maximum to negative infinity to handle all-negative trees
        self.max_sum = float('-inf')
        
        def get_max_gain(node):
            if not node:
                return 0
            
            # Recursively find the max gain from left and right subtrees
            # If a subtree returns a negative sum, ignore it by clamping to 0
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Price of the path if the current node acts as the highest pivot point (split)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum found so far
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the maximum single branch sum back up to the parent node
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return self.max_sum

        