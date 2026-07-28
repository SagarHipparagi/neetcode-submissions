class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A tree with n nodes must have exactly n-1 edges
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Check if all nodes were visited
        return len(visited) == n