class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        Generates all combinations of well-formed parentheses for a given n pairs.
        """
        result = []
        
        def backtrack(current_string: str, open_count: int, close_count: int):
            # Base case: if the string reaches the required length (2 * n)
            if len(current_string) == 2 * n:
                result.append(current_string)
                return
            
            # Rule 1: Add an opening parenthesis if we haven't used all 'n'
            if open_count < n:
                backtrack(current_string + "(", open_count + 1, close_count)
                
            # Rule 2: Add a closing parenthesis if it matches an existing open one
            if close_count < open_count:
                backtrack(current_string + ")", open_count, close_count + 1)

        # Initialize backtracking
        backtrack("", 0, 0)
        return result

