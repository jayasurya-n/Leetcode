from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        srange = [-sys.maxsize,sys.maxsize]
        maxi = -sys.maxsize
        
        for i in range(len(nums)):
            heapq.heappush(pq,(nums[i][0],i,0))
            maxi = max(maxi,nums[i][0])
        
        while pq:
            mini,row,col = heapq.heappop(pq)
            if(maxi-mini<srange[1]-srange[0]):srange = [mini,maxi]

            if(col==len(nums[row])-1):break
            next = nums[row][col+1]
            heapq.heappush(pq,(next,row,col+1))
            maxi = max(maxi,next)
        
        return srange
            
# time complexity: O(nlogk)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))