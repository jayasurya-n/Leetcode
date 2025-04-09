from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        mini = min(nums)
        if(k>mini):return -1
        
        hash = set()
        for num in nums:hash.add(num)
        return len(hash) if k<mini else len(hash)-1

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))