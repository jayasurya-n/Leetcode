from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        def dfs(i):
            if(i<0 or i>=n or visited[i]):return False
            if(arr[i]==0):return True
            visited[i] = True
            ans = False
            return dfs(i+arr[i]) or dfs(i-arr[i])
        
        visited = [False]*n
        return dfs(start)
        
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))