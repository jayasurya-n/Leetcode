from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-97]+=1
        
        odd,even = 1,len(s)+1
        for i in range(26):
            if(freq[i]==0):continue
            if(freq[i]%2==0):even = min(even,freq[i])
            else:odd = max(odd,freq[i])
        return odd-even
        
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))