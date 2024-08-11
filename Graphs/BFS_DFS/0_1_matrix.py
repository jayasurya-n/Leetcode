from typing import List,Optional
from collections import deque
import sys
class Solution:
    def updateMatrix(self, mat: List[List[int]]):
        m,n = len(mat),len(mat[0])
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def bfs(start):
            q = deque()
            for pair in start:
                visited[pair[0]][pair[1]] = True
                q.append(pair)
            
            while(q):
                i,j,d = q.popleft()
                distance[i][j] = d
                for k in range(4):
                    x = i+dx[k]
                    y = j+dy[k]
                    if(x<m and x>=0 and 
                       y<n and y>=0 and 
                       not visited[x][y]):
                        visited[x][y] = True
                        q.append((x,y,d+1))
            
            
        visited = [[False]*n for _ in range(m)]
        distance = [[0]*n for _ in range(m)]
        start = []
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==0):start.append((i,j,0))
        
        bfs(start)
        return distance
    
# time complexity: O(4mn+mn)
# space complexity: O(3mn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))