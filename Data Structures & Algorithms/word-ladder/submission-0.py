from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        if endWord not in wordList:
            return 0
        
        word_len = len(beginWord)
        patterns = defaultdict(list)
        
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)
                
        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        
        while queue:
            current_word, level = queue.popleft()
            
            if current_word == endWord:
                return level
                
            for i in range(word_len):
                pattern = current_word[:i] + "*" + current_word[i+1:]
                
                for neighbor in patterns[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))
                        
                # Optional optimization: clear processed patterns
                if pattern in patterns:
                    del patterns[pattern]
                
        return 0


        