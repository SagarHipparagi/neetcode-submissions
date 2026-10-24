class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # There are n nodes labeled 1 to n, and n edges
        n = len(edges)
        
        # Initialize each node as its own parent
        parent = list(range(n + 1))
        # Initialize rank of each node to 1 for optimization
        rank = [1] * (n + 1)
        
        def find(node: int) -> int:
            """Finds the ultimate root parent of a node with path compression."""
            if parent[node] != node:
                parent[node] = find(parent[node])  # Path compression
            return parent[node]
            
        def union(node1: int, node2: int) -> bool:
            """
            Unites two disjoint sets. 
            Returns True if united successfully, False if they already share a parent (cycle).
            """
            root1 = find(node1)
            root2 = find(node2)
            
            if root1 == root2:
                return False  # A cycle is detected
                
            # Union by rank optimization
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
                
            return True

        # Process each edge sequentially
        for u, v in edges:
            if not union(u, v):
                # The first edge that breaks the union operation completes a cycle.
                # Since we process sequentially, this naturally handles the "last occurrence" rule.
                return [u, v]
                
        return []

        