import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        
        # Turn the initial list into a valid min-heap in O(N) time
        heapq.heapify(self.min_heap)
        
        # Shrink the heap until it only holds the k largest elements
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Push the new value onto the min-heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap size exceeds k, pop the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the min-heap is the kth largest element so far
        return self.min_heap[0]

        
