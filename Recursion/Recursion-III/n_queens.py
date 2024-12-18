from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def solveNQueens(self, n: int) -> List[List[str]]:
        # board = [['.']*n for _ in range(n)]
        # ans = []
        
        # def isPossible(x,y):
        #     i,j = x,y
        #     while(i>=0 and j>=0):
        #         if(board[i][j]=='Q'):return False
        #         i-=1
        #         j-=1
                
        #     i,j = x,y
        #     while(j>=0):
        #         if(board[i][j]=='Q'):return False
        #         j-=1
            
        #     i,j = x,y
        #     while(i<n and j>=0):
        #         if(board[i][j]=='Q'):return False
        #         i+=1
        #         j-=1
            
        #     return True
            
        # def rec(col):
        #     if(col>=n):
        #         ans.append(["".join(row) for row in board])
        #         return 
            
        #     for i in range(n):
        #         if(isPossible(i,col)):
        #             board[i][col] = 'Q'
        #             rec(col+1)
        #             board[i][col] = '.'
            
        # rec(0)
        # return ans
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        ans = []
        
        row = [0]*n
        ld = [0]*(2*n-1)
        ud = [0]*(2*n-1)
        
        def rec(col):
            if(col>=n):
                ans.append(["".join(row) for row in board])
                return 
            
            for i in range(n):
                if(row[i]==0 and ld[i+col]==0 and ud[n-1+col-i]==0):
                    row[i] = 1
                    ld[i+col] = 1
                    ud[n-1+i-col] = 1
                    board[i][col] = 'Q'
                    rec(col+1)
                    board[i][col] = '.'
                    row[i] = 0
                    ld[i+col] = 0
                    ud[n-1+i-col] = 0
            
        rec(0)
        return ans
        

# time complexity: O(n!*n),O(n!)
# space complexity: O(n^2),O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))