from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        ntimes = sorted((times[i][0],times[i][1],i) for i in range(n))
        chairs = list(range(n))
        ends = []
        heapq.heapify(chairs)
        
        for i in range(n):
            s,e,ind = ntimes[i]
            while(ends and s>=ends[0][0]):
                _,chair = heapq.heappop(ends)
                heapq.heappush(chairs,chair)
            
            chair = heapq.heappop(chairs)
            heapq.heappush(ends,(e,chair))
            
            if(ind==targetFriend):return chair
                
# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))