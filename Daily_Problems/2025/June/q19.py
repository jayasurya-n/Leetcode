from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 1
        start = nums[0]
        for i in range(1,len(nums)):
            if(nums[i]-start>k):
                cnt+=1
                start = nums[i]
        return cnt

# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))