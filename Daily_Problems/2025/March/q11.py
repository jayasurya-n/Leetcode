from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        i = j = 0
        ans = 0
        count = [0]*3
        
        while(j<n):
            count[ord(s[j])-97]+=1
            
            while(i<j and count[0]>=1 and count[1]>=1 and count[2]>=1):
                ans+=n-j
                count[ord(s[i])-97]-=1
                i+=1
            
            j+=1
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))