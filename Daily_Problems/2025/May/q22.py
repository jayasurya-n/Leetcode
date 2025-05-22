from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort(key = lambda x:x[0])
        diff = [0]*(n+1)
        end_pq = [] 
        ope = j = 0

        for i in range(n):
            ope+=diff[i]
            while j<len(queries) and queries[j][0]==i:
                heapq.heappush(end_pq,-queries[j][1])
                j+=1
            
            while end_pq and ope<nums[i] and -end_pq[0]>=i:
                ope+=1
                diff[-heapq.heappop(end_pq)+1]-=1
            
            if(ope<nums[i]):return -1
        
        return len(end_pq)

# time complexity: O(n+mlogm)
# space complexity: O(n+m)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))