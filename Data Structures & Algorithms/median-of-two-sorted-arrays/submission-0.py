class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search runtime
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        # Binary search boundaries on the smaller array
        low, high = 0, m
        
        while low <= high:
            # Partition index for nums1
            i = (low + high) // 2
            # Partition index for nums2 to ensure the left side has 'half' elements
            j = half - i
            
            # Boundary values around the partition line (handling out-of-bounds with infinity)
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                # If total elements is odd, return the minimum of the right elements
                if total % 2 != 0:
                    return float(min(right1, right2))
                # If even, return the average of the maximum left and minimum right elements
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            
            # If we are too far right in nums1, move the partition left
            elif left1 > right2:
                high = i - 1
            # If we are too far left in nums1, move the partition right
            else:
                low = i + 1
                
        return 0.0

        