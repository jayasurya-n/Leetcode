from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countLargestGroup(self, n: int) -> int:
        hash = [0]*37
        for num in range(1,n+1):
            sum = 0
            while num:
                sum+=num%10
                num//=10
            hash[sum]+=1
        
        return hash.count(max(hash))

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))