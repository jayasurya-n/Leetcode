from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        for i in range(len(num)-2):
            if num[i]==num[i+1] and num[i]==num[i+2]:
                ans = max(ans,int(num[i]))
        
        return str(ans)*3 if ans!=-1 else ''

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))