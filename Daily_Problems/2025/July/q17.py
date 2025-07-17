from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i][rem]: max length subsequnce ending at i with reminder rem
        dp = [[0]*k for _ in range(n)]
        
        for i in range(1,n):
            for j in range(i):
                rem = (nums[i]+nums[j])%k
                dp[i][rem] = max(dp[i][rem],dp[j][rem]+1)
        return 1+max(max(row) for row in dp)

# time complexity: O(nk)
# space complexity: O(nk)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))