# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_val: int) -> int:
            if not node:
                return 0
            
            # Check if current node is a "good" node
            current_good = 1 if node.val >= max_val else 0
            
            # Update the maximum value for the path going forward
            max_val = max(max_val, node.val)
            
            # Sum up results from the current node, left subtree, and right subtree
            return current_good + dfs(node.left, max_val) + dfs(node.right, max_val)
        
        # Start DFS with the root node and its own value as the initial maximum path value
        return dfs(root, root.val)

        