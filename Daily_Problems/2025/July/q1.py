from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def possibleStringCount(self, word: str) -> int:
        curr = word[0]
        ans = cnt = 0
        for ch in word:
            if(ch==curr):cnt+=1
            else:
                ans+=cnt-1
                cnt=1
                curr = ch
        
        ans+=cnt-1
        return ans+1

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))