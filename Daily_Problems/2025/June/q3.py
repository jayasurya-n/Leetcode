from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        boxes_found = [False]*n
        keys_found = [False]*n
        total_candy = 0

        q = deque([])
        for box in initialBoxes:
            boxes_found[box] = True
            if(status[box]):
                q.append(box)

        while q:
            box = q.popleft()
            if(status[box]==2):continue
            status[box] = 2
            total_candy+=candies[box]

            for ind in keys[box]:
                keys_found[ind] = True
                if(boxes_found[ind] and status[ind]!=2):
                    q.append(ind)
            
            for ind in containedBoxes[box]:
                boxes_found[ind] = True
                if(status[ind]==1 or (keys_found[ind] and status[ind]!=2)):
                    q.append(ind)

        return total_candy

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))