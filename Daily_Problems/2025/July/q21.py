from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def makeFancyString(self, s: str) -> str:
        curr = s[0]
        cnt = 0
        ans  = []
        for ch in s:
            if(ch==curr):cnt+=1
            else:
                curr = ch
                cnt = 1
            if(cnt<=2):ans.append(ch)
        return "".join(ans)

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))