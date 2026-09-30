class TreeNode:
    """Represents a node in the binary tree."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # A helper function that returns the height of the tree if balanced,
        # or -1 if any subtree is found to be unbalanced.
        def check_height(node: TreeNode) -> int:
            if not node:
                return 0  # Base case: an empty tree has a height of 0
            
            # 1. Check the left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1  # Early exit: left subtree is already unbalanced
            
            # 2. Check the right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1  # Early exit: right subtree is already unbalanced
            
            # 3. Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is unbalanced
            
            # If balanced, return the actual height of this node
            return max(left_height, right_height) + 1

        # If check_height doesn't return -1, the tree is balanced
        return check_height(root) != -1

# --- Example Usage ---
if __name__ == "__main__":
   
    balanced_root = TreeNode(1)
    balanced_root.left = TreeNode(2)
    balanced_root.right = TreeNode(3)
    balanced_root.left.left = TreeNode(4)

    
    unbalanced_root = TreeNode(1)
    unbalanced_root.left = TreeNode(2)
    unbalanced_root.left.left = TreeNode(3)

    solution = Solution()
    print(f"Is tree 1 balanced? {solution.isBalanced(balanced_root)}")    # Output: True
    print(f"Is tree 2 balanced? {solution.isBalanced(unbalanced_root)}")  # Output: False

        