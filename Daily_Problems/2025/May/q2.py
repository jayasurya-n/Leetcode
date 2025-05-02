from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        effect = [0]*n
        
        curr = 0
        for i in range(n):
            if(dominoes[i]=='R'):curr = n
            elif(dominoes[i]=='L'):curr = 0
            else:curr = max(curr-1,0)
            effect[i]+=curr
        
        curr = 0
        for i in range(n-1,-1,-1):
            if(dominoes[i]=='L'):curr = n
            elif(dominoes[i]=='R'):curr = 0
            else:curr = max(curr-1,0)
            effect[i]-=curr
        
        
        ans = []
        for i in range(n):
            if(effect[i]>0):ans.append('R')
            elif(effect[i]<0):ans.append('L')
            else:ans.append('.')
        return "".join(ans)

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))