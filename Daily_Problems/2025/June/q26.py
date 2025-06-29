from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = 0
        val = 0
        for i in range(len(s)-1,-1,-1):
            if(s[i]=='0'):ans+=1
            elif(s[i]=='1'):
                if((1<<ans)+val<=k):
                    val+=1<<ans
                    ans+=1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))