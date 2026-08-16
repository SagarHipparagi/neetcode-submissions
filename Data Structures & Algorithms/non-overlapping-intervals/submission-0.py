class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        count = 0
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start >= prev_end:
                # No overlap
                prev_end = end
            else:
                # Overlap
                count += 1

        return count