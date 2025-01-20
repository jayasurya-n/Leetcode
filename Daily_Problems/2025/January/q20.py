from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m,n = len(mat),len(mat[0])
        hash = defaultdict(int)
        
        for i in range(m):
            for j in range(n):
                hash[mat[i][j]] = (i,j)

        row = [0]*m
        col = [0]*n
        for k,num in enumerate(arr):
            i,j = hash[num]
            row[i]+=1
            col[j]+=1
            if(row[i]==n or col[j]==m):return k 

# time complexity: O(mn)
# space complexity: O(mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))