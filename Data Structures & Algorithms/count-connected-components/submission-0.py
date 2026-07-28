class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list
        graph = {}

        for i in range(n):
            graph[i] = []

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        # Step 2: Visit every node
        for node in range(n):
            if node not in visited:
                dfs(node)
                components += 1

        return components