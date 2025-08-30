from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False]*10 for _ in range(9)]
        cols = [[False]*10 for _ in range(9)]
        threes = [[False]*10 for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if(board[i][j]=='.'):continue
                num = int(board[i][j])
                k = 3*(i//3)+(j//3)
                if(rows[i][num] or cols[j][num] or threes[k][num]):return False
                rows[i][num] = cols[j][num] = threes[k][num] = True
        return True
    
# time complexity: O(9^2)
# space complexity: O(9^2)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))