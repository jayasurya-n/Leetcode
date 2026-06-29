from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        gcd = 0
        for num in nums:
            gcd = math.gcd(num,gcd)

        if(gcd!=1):return -1

        ans = n+1
        for i in range(n):
            gcd = 0
            for j in range(i,n):
                gcd = math.gcd(gcd,nums[j])
                if(gcd==1):
                    ans = min(ans,j-i+1)
                    break
        return n+ans-2 


# time complexity: O(n^2logM)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))