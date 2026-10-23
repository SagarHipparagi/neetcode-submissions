class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Step 1: Build adjacency list
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            
        # 0 = unvisited, 1 = visiting, 2 = visited
        visit = [0] * numCourses
        order = []
        
        def dfs(course):
            if visit[course] == 1:  # Cycle detected
                return False
            if visit[course] == 2:  # Already fully processed
                return True
                
            visit[course] = 1  # Mark as visiting
            
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
                    
            visit[course] = 2  # Mark as fully processed
            order.append(course)  # Add to topological order
            return True

        # Step 2: Run DFS for each course
        for i in range(numCourses):
            if not dfs(i):
                return []  # Return empty list if a cycle is found
                
        # Step 3: Reverse the order since post-order DFS yields courses backwards
        return order[::-1]

        