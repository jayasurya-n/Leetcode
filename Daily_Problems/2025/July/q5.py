from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n = len(arr)
        freq = [0]*(n+1)
        for num in arr:
            if(0<num<=n):freq[num]+=1
        
        ans = -1
        for num in range(1,n+1):
            if(num==freq[num]):ans = num
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))