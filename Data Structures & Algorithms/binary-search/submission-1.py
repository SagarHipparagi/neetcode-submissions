from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Performs a binary search on a sorted list of integers.
        Returns the index of the target if found, otherwise returns -1.
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # Calculate the middle index (prevents integer overflow)
            mid = left + (right - left) // 2
            
            # Check if target is present at mid
            if nums[mid] == target:
                return mid
            
            # If target is greater, ignore the left half
            elif nums[mid] < target:
                left = mid + 1
                
            # If target is smaller, ignore the right half
            else:
                right = mid - 1
                
        # Element was not present in the array
        return -1


# ==========================================
# Driver / Execution Code (The "main" block)
# ==========================================
if __name__ == "__main__":
    # 1. Instantiate the class (This is line 55 where your traceback occurred)
    solution = Solution()
    
    # 2. Define test variables (Array MUST be sorted)
    sorted_array = [-1, 0, 3, 5, 9, 12]
    target_value = 9
    
    # 3. Call the method and store the result
    result = solution.search(sorted_array, target_value)
    
    # 4. Print output
    print(f"Target {target_value} found at index: {result}") 
    # Expected Output: Target 9 found at index: 4

