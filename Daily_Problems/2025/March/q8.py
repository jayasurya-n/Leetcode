from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        i = j = 0
        whites = 0
        ans = n+1
        while(j<n):
            if(blocks[j]=='W'):whites+=1
            
            while(i<j and j-i+1>k):
                if(blocks[i]=='W'):whites-=1
                i+=1
        
            if(j-i+1==k):ans = min(ans,whites)
            j+=1
        
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))