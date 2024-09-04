from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        mul = 6*(10**4)+1
        st = set()
        for x,y in obstacles:st.add(x+y*mul)
        
        ans = 0
        dir = 0
        x,y = 0,0
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in range(len(commands)):
            l = commands[i]
            if(l==-1):dir = (dir+1)%4
            elif(l==-2):dir = (dir+3)%4
            else:
                dx,dy = directions[dir]
                for _ in range(l):
                    nx,ny = x+dx,y+dy
                    if((nx+ny*mul) in st):break
                    x,y = nx,ny
                
                ans = max(ans,x*x+y*y)
        
        return ans
    
# time complexity: O(m+n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))