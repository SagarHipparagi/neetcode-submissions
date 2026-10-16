class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # Handle edge case: empty input string
        if not digits:
            return []
            
        # Define the phone keypad mapping
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        combinations = []
        
        def backtrack(index: int, current_path: list):
            # Base case: if the current combination is complete
            if len(current_path) == len(digits):
                combinations.append("".join(current_path))
                return
            
            # Get the possible letters for the current digit
            possible_letters = phone_map[digits[index]]
            
            for letter in possible_letters:
                # 1. Choose the letter
                current_path.append(letter)
                # 2. Explore next digit combinations
                backtrack(index + 1, current_path)
                # 3. Backtrack (remove the letter to try the next one)
                current_path.pop()
                
        # Start the backtracking process from index 0
        backtrack(0, [])
        return combinations

        