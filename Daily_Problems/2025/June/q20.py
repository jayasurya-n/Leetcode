from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxDistance(self, string: str, k: int) -> int:
        n = s = e = w = 0
        ans = 0
        for ch in string:
            if(ch=='N'):n+=1
            if(ch=='S'):s+=1
            if(ch=='E'):e+=1
            if(ch=='W'):w+=1
            ans = max(ans,abs(n-s)+abs(e-w)+
                      2*(min(k,min(n,s)+min(e,w))))
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))   