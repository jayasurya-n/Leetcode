from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        visited = set()
        q = deque([(1,0)])

        while q:
            sq,moves = q.popleft()
            for i in range(1,7):
                next_sq = sq+i
                if(next_sq>n*n):continue
                r,c = (next_sq-1)//n, (next_sq-1)%n
                if(r%2==1):c = n-1-c

                if(board[r][c]!=-1):
                    next_sq = board[r][c]
                
                if(next_sq==n*n):return moves+1
                if(next_sq not in visited):
                    visited.add(next_sq)
                    q.append((next_sq,moves+1))
        return -1
    
# time complexity: O(n^2)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))