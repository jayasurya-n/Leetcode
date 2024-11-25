from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj = {
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }
        
        target = "123450"
        start = "".join(str(num) for row in board for num in row)
        visisted = {start}
        q = deque([start])
        moves = 0
        
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if(curr==target):return moves
                
                ind = curr.index('0')
                for v in adj[ind]:
                    new_state = list(curr)
                    new_state[v],new_state[ind] = new_state[ind],new_state[v]
                    new_state = "".join(new_state)
                    if new_state not in visisted:
                        q.append(new_state)
                        visisted.add(new_state)
            moves+=1
        return -1
            
# time complexity: O((mn)!)
# space complexity: O((mn)!)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))