from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        strongest = [True]*n
        for u,v in edges:strongest[v] = False
        
        cnt = 0
        ans = -1
        for i in range(n):
            if(strongest[i]):
                cnt+=1
                ans = i
        
        return ans if cnt==1 else -1

# time complexity: O(n+m)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))