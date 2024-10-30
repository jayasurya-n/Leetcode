from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for i in range(len(nums)):
            heapq.heappush(pq,nums[i])
            if(len(pq)>k):heapq.heappop(pq)
        return pq[0]
    
# time complexity: O(nlogk)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))