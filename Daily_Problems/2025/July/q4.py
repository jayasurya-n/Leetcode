from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        length = 1<<len(operations)

        shifts = 0
        for ope in reversed(operations):
            half = length>>1
            if(k>half and ope==1):shifts+=1
            if(k>half):k-=half
            length = half
        
        shifts%=26
        return chr(97+shifts)

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))