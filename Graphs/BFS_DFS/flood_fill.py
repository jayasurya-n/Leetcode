from typing import List,Optional
from collections import deque
import sys
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int):
        m = len(image)
        n = len(image[0])
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def dfs(i,j):
            image[i][j] = color
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if(x<m and x>=0 and 
                   y<n and y>=0 and 
                   image[x][y]==original): dfs(x,y)
        
        original = image[sr][sc]
        dfs(sr,sc)
        return image

# time complexity: O(m*n)
# space complexity: O(m*n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        image = [list(map(int,input().strip().split())) for _ in range(m)]
        sr,sc = list(map(int,input().strip().split()))
        color = int(input().strip())
        print(Solution().floodFill(image,sr,sc,color))