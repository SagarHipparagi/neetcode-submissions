import heapq

class MedianFinder:

    def __init__(self):
        # max_heap stores the smaller half of the numbers (inverted to simulate max-heap)
        self.max_heap = []
        # min_heap stores the larger half of the numbers
        self.min_heap = []

    def addNum(self, num: int) -> None:
        # Step 1: Always push to max_heap first (negate to maintain max-heap property)
        heapq.heappush(self.max_heap, -num)
        
        # Step 2: Balance check - ensure all elements in max_heap <= min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
            
        # Step 3: Size check - maintain size difference of at most 1 element
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        # If one heap has more elements, its top element is the median
        if len(self.max_heap) > len(self.min_heap):
            return float(-self.max_heap[0])
        elif len(self.min_heap) > len(self.max_heap):
            return float(self.min_heap[0])
        
        # If heaps are equal size, median is the average of both roots
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0



        


        


        
        