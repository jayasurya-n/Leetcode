from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        ans = cnt = 0
        i = 0
        while i<n:
            if(s[i]=='0'):
                i+=1
                continue
            
            ones = 0
            while(i<n and s[i]=='1'):
                ones+=1
                i+=1
            
            if(i<n):
                cnt+=ones
                ans+=cnt
            
            i+=1
            
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))