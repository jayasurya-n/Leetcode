from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a = b = c = -1
        ans = 0
        for i,ch in enumerate(s):
            if(ch=='a'):a = i
            elif(ch=='b'):b = i
            else:c = i
            ans+=min(a,b,c)+1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))