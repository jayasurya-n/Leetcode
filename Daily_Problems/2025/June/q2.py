from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        ans = [1]*n

        for i in range(1,n):
            if(ratings[i]>ratings[i-1]):
                ans[i] = ans[i-1]+1
        
        for i in range(n-2,-1,-1):
            if(ratings[i]>ratings[i+1]):
                ans[i] = max(ans[i],1+ans[i+1])
        
        return sum(ans)

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        ratings = lii()
        print(Solution().candy(ratings,n))