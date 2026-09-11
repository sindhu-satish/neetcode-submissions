import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = r
        
        while l <= r:
            m = (l + r) // 2
            num_of_h = 0
            for pile in piles:
                num_of_h += math.ceil(float(pile)/m)
            
            if num_of_h <= h:
                res = m
                r = m - 1
            elif num_of_h > h:
                l = m + 1

        return res

        
