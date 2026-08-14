class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for interval in intervals:
            start, end = interval
            
            # New interval comes after this interval
            if end < newInterval[0]:
                result.append(interval)
            
            # New interval comes before this interval
            elif start > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            
            # They overlap -> merge
            else:
                newInterval[0] = min(newInterval[0], start)
                newInterval[1] = max(newInterval[1], end)
        
        result.append(newInterval)
        
        return result