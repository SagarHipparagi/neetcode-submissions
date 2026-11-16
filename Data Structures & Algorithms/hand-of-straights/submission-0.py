from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Total cards must be evenly divisible by groupSize
        if len(hand) % groupSize != 0:
            return False
            
        count = Counter(hand)
        
        # Iterate through the unique card values in sorted order
        for card in sorted(count):
            needed = count[card]
            if needed > 0:
                # Form 'needed' groups starting with the current smallest card
                for i in range(groupSize):
                    current_card = card + i
                    if count[current_card] < needed:
                        return False
                    count[current_card] -= needed
                    
        return True

        