from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if(n%2==1):ans.append(0)
        
        curr = 1
        while len(ans)<n:
            ans.append(curr)
            ans.append(-curr)
            curr+=1
        
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))