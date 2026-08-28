class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

# 2. SOLUTION CLASS FOLLOWS
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # Step 1: Build the Trie
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            
        # Core fix: properly capture rows and columns for non-square grids
        rows = len(board)
        cols = len(board[0]) if rows > 0 else 0
        result = []
        
        # Step 2: Backtracking (DFS) function
        def dfs(r, c, parent_node):
            char = board[r][c]
            curr_node = parent_node.children[char]
            
            # If a word is found, add it to results
            if curr_node.word:
                result.append(curr_node.word)
                curr_node.word = None  # Prevent duplicate matches
                
            # Temporarily mark the cell as visited
            board[r][c] = "#"
            
            # Explore 4 directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node.children:
                    dfs(nr, nc, curr_node)
                    
            # Backtrack: restore the original character
            board[r][c] = char
            
            # Optimization: Prune the node if it has no children left
            if not curr_node.children:
                parent_node.children.pop(char)

        # Step 3: Traverse every cell on the board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
                    
        return result