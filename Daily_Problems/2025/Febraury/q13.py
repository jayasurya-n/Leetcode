from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = nums
        heapq.heapify(pq)
        ans = 0
        while pq[0]<k and len(pq)>1:
            f = heapq.heappop(pq)
            s = heapq.heappop(pq)
            heapq.heappush(pq,s+2*f)
            ans+=1
        return ans if pq[0]>=k else -1

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))