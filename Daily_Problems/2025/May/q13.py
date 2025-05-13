from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        # mod = 10**9+7
        # freq = [0]*26
        # for ch in s:freq[ord(ch)-97]+=1
        
        # ans = len(s)
        # for _ in range(t):
        #     last = freq[25]
        #     for i in range(25,0,-1):
        #         freq[i] = freq[i-1]
            
        #     freq[0] = last
        #     freq[1]+=last
        #     freq[1]%=mod
            
        #     ans+=last
        #     ans%=mod
        
        # return ans

        mod = 10**9+7
        freq = deque([0]*26)
        for ch in s:freq[ord(ch)-97]+=1
        
        ans = len(s)
        for _ in range(t):
            last = freq.pop()
            freq.appendleft(last)
            
            freq[1]+=last
            freq[1]%=mod
            
            ans+=last
            ans%=mod
        
        return ans

# time complexity: O(26*t),O(t)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        s = si()
        t = ii()
        print(Solution().lengthAfterTransformations(s,t))