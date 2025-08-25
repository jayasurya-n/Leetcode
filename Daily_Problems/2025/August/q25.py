from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # m,n = len(mat),len(mat[0])
        # ans = []
        # dir = 1

        # for c in range(0,m+n-1):
        #     if(dir==1):
        #         for i in range(m-1,-1,-1):
        #             j = c-i
        #             if(j>=n):continue
        #             ans.append(mat[i][j])
        #     else:
        #         for i in range(m):
        #             j = c-i
        #             if(j>=n):continue
        #             ans.append(mat[i][j])
        #     dir*=-1
        
        # return ans

        m,n = len(mat),len(mat[0])
        ans = []
        i = j = 0
        dir = 1
        while i<m and j<n:
            ans.append(mat[i][j])
            if(dir==1):ni,nj = i-1,j+1
            else:ni,nj = i+1,j-1

            if(ni<0 or ni>=m or nj<0 or nj>=n):
                if(dir==1):
                    if(j+1<n):ni,nj = i,j+1
                    else:ni,nj = i+1,j
                else:
                    if(i+1<m):ni,nj = i+1,j
                    else:ni,nj = i,j+1
                dir*=-1
            i,j = ni,nj
        return ans

# time complexity: O(mn),O(mn)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))