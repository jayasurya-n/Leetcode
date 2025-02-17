from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def rec(hash): 
            total = 0
            for ch in hash.keys():
                if(hash[ch]==0):continue
                hash[ch]-=1
                total+=1+rec(hash)
                hash[ch]+=1
            return total
        hash = defaultdict(int)
        for ch in tiles:hash[ch]+=1
        return rec(hash)

# time complexity: O(n!)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))