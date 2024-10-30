from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        hash = defaultdict(int)
        for val in hand:hash[val]+=1

        for val in hand:
            if(hash[val]<=0):continue
            size=0
            while hash[val]>0 and size<groupSize:
                hash[val]-=1
                val+=1
                size+=1
            if(size!=groupSize):return False
        return True
        
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))