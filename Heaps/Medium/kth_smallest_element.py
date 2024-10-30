from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def kthSmallest(self, arr,k):
        pq = []
        for i in range(len(arr)):
            heapq.heappush(pq,-arr[i])
            if(len(pq)>k):heapq.heappop(pq)
        return -pq[0]
    
# time complexity: O(nlogk)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))