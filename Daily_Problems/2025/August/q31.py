from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False]*10 for _ in range(9)]
        cols = [[False]*10 for _ in range(9)]
        threes = [[False]*10 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):continue
                num = int(board[i][j])
                k = 3*(i//3)+(j//3)
                rows[i][num] = cols[j][num] = threes[k][num] = True

        def solve(i,j):
            if(i>=9):return True
            if(board[i][j]!='.'):
                return solve(i+(j+1)//9,(j+1)%9)

            k = 3*(i//3)+(j//3)
            for num in range(1,10):
                if(rows[i][num] or cols[j][num] or threes[k][num]):continue
                rows[i][num] = cols[j][num] = threes[k][num] = True
                board[i][j] = str(num)

                if(solve(i+(j+1)//9,(j+1)%9)):return True

                board[i][j] = '.'
                rows[i][num] = cols[j][num] = threes[k][num] = False
            
            return False

        solve(0,0)

# time complexity: O(9^81)
# space complexity: O(81)
if __name__ == "__main__":
    for _ in range(ii()):
        board = [lsi() for _ in range(9)] 
        Solution().solveSudoku(board)
        for row in board:print(row)