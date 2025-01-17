from typing import List,Optional
from collections import deque
import sys
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int):
        
        i,j = rStart,cStart
        ans = [[i,j]]
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        
        dir = 0
        steps = 1
        while(len(ans)<rows*cols):
            for _ in range(2):
                for _ in range(steps):
                    i+=dx[dir]
                    j+=dy[dir]
                    if(0<=i<rows and 0<=j<cols):ans.append([i,j])
                dir+=1
                dir%=4
            steps+=1
        return ans
# time complexity: O(mn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))