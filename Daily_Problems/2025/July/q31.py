from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        curr = set()
        ans = set()
        for x in arr:
            curr = {x}|{x|y for y in curr}
            ans|=curr
        return len(ans)

# time complexity: O(32n)
# space complexity: O(32n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))