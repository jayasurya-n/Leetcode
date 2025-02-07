from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        hash = defaultdict(int)
        map = defaultdict(int)
        ans = []
        for ball,color in queries:
            if(ball in map):
                old_color = map[ball]
                hash[old_color]-=1
                if(hash[old_color]==0):hash.pop(old_color)    
            hash[color]+=1
            map[ball] = color
            ans.append(len(hash))
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))