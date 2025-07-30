from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        ans = cnt = 0
        for num in nums:
            if(num==max_and):cnt+=1
            else:cnt = 0
            ans = max(ans,cnt)
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))