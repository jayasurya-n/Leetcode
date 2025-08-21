from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        # m,n = len(mat),len(mat[0])
        # dp = [[0]*n for _ in range(m)]

        # def solve(x,y):
        #     ans = 0      
        #     prev = m+n
        #     for j in range(y,-1,-1):
        #         if(mat[x][j]==1):dp[x][j] =  (dp[x-1][j] if x>0 else 0)+1 
        #         else:dp[x][j] = 0 
        #         prev = min(prev,dp[x][j])
        #         ans+=prev
        #     return ans

        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         ans+=solve(i,j)
        # return ans

        m,n = len(mat),len(mat[0])
        ans = 0
        heights = [0]*n
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==1):heights[j]+=1
                else:heights[j] = 0
            
            count = [0]*n
            stack = []
            for j in range(n):
                while stack and heights[stack[-1]]>=heights[j]:stack.pop()
                if(stack):count[j] = count[stack[-1]]+(j-stack[-1])*heights[j]
                else:count[j] = (j+1)*heights[j]
                ans+=count[j]
                stack.append(j)
        return ans

# time complexity: O(mn^2),O(mn)
# space complexity: O(mn),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        m,n = lii()
        mat = []
        for _ in range(n):
            mat.append(lii())
        print(Solution().numSubmat(mat))