import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # Initialize an empty min-heap
        min_heap = []
        
        for num in nums:
            # Push the current number onto the min-heap
            heapq.heappush(min_heap, num)
            
            # If the heap size exceeds k, pop the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        # The top of the min-heap is now the kth largest element
        return min_heap[0]

        