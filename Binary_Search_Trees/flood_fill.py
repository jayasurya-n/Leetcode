from typing import List,Optional
from collections import deque
import sys
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int):
        m = len(image)
        n = len(image[0])
        def solve(x,y):
            if(x<0 or x>=m or y<0 or y>=n or 
            image[x][y]!=original or image[x][y]==color):return 

            image[x][y] = color
            solve(x+1,y) 
            solve(x-1,y)
            solve(x,y+1) 
            solve(x,y-1)

        original = image[sr][sc]
        solve(sr,sc)
        return image

# time complexity: O(m*n)
# space complexity: O(m*n(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))