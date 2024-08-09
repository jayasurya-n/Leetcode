from typing import List,Optional
from collections import deque
import sys
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]):
        m,n = len(grid),len(grid[0])
        
        def isMagicSqaure(x,y):
            hash = [0]*9
            for i in range(3):
                for j in range(3):
                    num = grid[x+i][y+j]
                    if(num>9 or num<1):return False
                    if(hash[num-1]!=0):return False
                    hash[num-1]=1
                    

            d1 = grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2]
            d2 = grid[x+2][y] + grid[x+1][y+1] + grid[x][y+2]
            if(d1!=d2):return False
            
            for i in range(3):
                r = grid[x+i][y] + grid[x+i][y+1] + grid[x+i][y+2]
                if(r!=d1):return False
            
            for j in range(3):
                c = grid[x][y+j] + grid[x+1][y+j] + grid[x+2][y+j]
                if(c!=d1):return False
            
            return True
                    
        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                if(isMagicSqaure(i,j)):ans+=1
        return ans
# time complexity: O(mn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))