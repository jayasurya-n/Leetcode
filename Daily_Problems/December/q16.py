from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        minheap = [(num,i) for i,num in enumerate(nums)]
        heapq.heapify(minheap)
        
        for _ in range(k):
            _,i = heapq.heappop(minheap)
            nums[i]*=multiplier
            heapq.heappush(minheap,(nums[i],i))
        return nums

# time complexity: O(klogn+n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))