from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        for num in nums:hash[num]+=1

        ans = 0
        for num in hash.keys():
            if(hash.get(num+1) is not None):
                ans = max(ans,hash[num]+hash[num+1])
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))