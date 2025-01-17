from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open,ans = 0,0
        for ch in s:
            if(ch=='('):open+=1
            else:
                if(open>0):open-=1
                else:ans+=1
        return ans+open

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))