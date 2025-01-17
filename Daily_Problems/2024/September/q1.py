from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if(len(original)!=m*n):return []
        
        ans = [[0]*n for _ in range(m)]
        for k in range(len(original)):
            i,j = k//n,k%n
            ans[i][j] = original[k]
        return ans

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        original = list(map(int,input().strip().split()))
        m,n = list(map(int,input().strip().split()))
        print(Solution().construct2DArray(original,m,n))