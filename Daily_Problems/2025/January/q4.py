from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        hash = defaultdict(lambda:[-1,-1])
        for i,ch in enumerate(s):
            if(hash[ch][0]==-1):hash[ch][0] = i
            else:hash[ch][1] = i
        
        ans = 0
        for ch,(start,end) in hash.items():
            hash = set()
            for i in range(start+1,end):hash.add(s[i])
            ans+=len(hash)
        return ans
                
# time complexity: O(26*n)
# space complexity: O(26)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))