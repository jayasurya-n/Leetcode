from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def findMaxsplit(index,hash):
            ans = 0
            for i in range(index,len(s)):
                if(s[index:i+1] in hash):continue
                hash.add(s[index:i+1])
                ans = max(ans,1+findMaxsplit(i+1,hash))
                hash.remove(s[index:i+1])
            return ans
         
        return findMaxsplit(0,set())
         
# time complexity: O(2^n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))