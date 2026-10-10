import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        """
        Initialize your data structures here.
        """
        self.count = 0  # Global timestamp tracker (decrements to act as a Max-Heap)
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set)   # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # We decrement count because Python's heapq is a min-heap by default.
        # Negative values ensure the newest tweets stay at the top.
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Retrieve the 10 most recent tweet IDs in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user themself.
        Tweets must be ordered from most recent to least recent.
        """
        res = []
        minHeap = []
        
        # Ensure the user sees their own tweets by adding themselves to the lookups
        self.followMap[userId].add(userId)
        
        # Gather the last tweet from each followee
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                # Push: (timestamp, tweetId, followeeId, next_index_to_look_at)
                minHeap.append([count, tweetId, followeeId, index - 1])
                
        # Convert our list into a valid heap structure
        heapq.heapify(minHeap)
        
        # Extract up to 10 most recent tweets
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If this user has older tweets left, push the next one into the heap
            if idx >= 0:
                nextCount, nextTweetId = self.tweetMap[followeeId][idx]
                heapq.heappush(minHeap, [nextCount, nextTweetId, followeeId, idx - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
