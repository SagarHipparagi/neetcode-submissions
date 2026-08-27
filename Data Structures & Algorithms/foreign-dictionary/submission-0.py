class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
         # Create graph and indegree for every character
        graph = defaultdict(list)
        indegree = {c: 0 for word in words for c in word}

        # Compare adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            # Invalid case: ["abc", "ab"]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # Find first different character
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    a = w1[j]
                    b = w2[j]

                    # a comes before b
                    graph[a].append(b)
                    indegree[b] += 1
                    break

        # Topological sort using BFS
        queue = deque()

        for char in indegree:
            if indegree[char] == 0:
                queue.append(char)

        result = []

        while queue:
            char = queue.popleft()
            result.append(char)

            for neighbor in graph[char]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Cycle detected
        if len(result) != len(indegree):
            return ""

        return "".join(result)