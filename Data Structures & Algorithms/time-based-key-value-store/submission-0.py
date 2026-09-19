from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        """
        Initializes the data structure.
        """
        # Maps each key to a list of tuples: (timestamp, value)
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key with the value at the given timestamp.
        Note: Timestamps are assumed to be strictly increasing.
        """
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        """
        Returns a value such that set was called previously, with timestamp_prev <= timestamp.
        Returns "" if no such value exists.
        """
        # If the key doesn't exist, return an empty string
        if key not in self.store:
            return ""
        
        values = self.store[key]
        
        # Binary search for the rightmost index where the entry's timestamp 
        # is less than or equal to the target timestamp.
        # We use a dummy tuple (timestamp, chr(255)) to safely search through pairs.
        idx = bisect.bisect_right(values, (timestamp, chr(255)))
        
        # If idx is 0, it means all stored timestamps are strictly greater than the target
        if idx == 0:
            return ""
            
        # Return the value from the matched (timestamp, value) tuple
        return values[idx - 1][1]

        
