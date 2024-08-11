from typing import List,Optional
from collections import deque
import sys
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m,n = len(board),len(board[0])
        
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        
        def dfs(i,j):
            visited[i][j] = True
            for k in range(4):
                x = i+dx[k]
                y = j+dy[k]
                if(x<m and x>=0 and 
                    y<n and y>=0 and 
                    not visited[x][y] and board[x][y]=='O'):
                    dfs(x,y)
            
        visited = [[False]*n for _ in range(m)]
        start = []
        for i in range(m):
            if(board[i][0]=='O' and not visited[i][0]):dfs(i,0) 
            if(board[i][-1]=='O' and not visited[i][-1]):dfs(i,n-1)
        
        for j in range(n):
            if(board[0][j]=='O' and not visited[0][j]):dfs(0,j)
            if(board[-1][j]=='O' and not visited[-1][j]):dfs(m-1,j)
            
        for i in range(m):
            for j in range(n):
                if(board[i][j]=='O' and not visited[i][j]):
                    board[i][j] = 'X'
        return board
    
# time complexity: O(4mn+m+n)
# space complexity: O(mn+mn(stack space))
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))