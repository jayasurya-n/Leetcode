from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        i = 0
        while i<len(s):
            ans.append(s[i:i+k])
            i+=k
        ans[-1]+=fill*(k-len(ans[-1]))
        return ans

# time complexity: O(max(n,k))
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))