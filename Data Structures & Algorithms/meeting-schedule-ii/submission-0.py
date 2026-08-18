"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        rooms = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            # Reuse a room if the previous meeting has ended
            if rooms and rooms[0] <= start:
                heapq.heappop(rooms)

            # Add current meeting's ending time
            heapq.heappush(rooms, end)

        return len(rooms)