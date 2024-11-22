from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hash = defaultdict(int)
        for row in matrix:
            key = tuple(row)
            if(row[0]==1):key = tuple([1-x for x in row])
            hash[key]+=1
        return max(hash.values()) 

# time complexity: O(mn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))