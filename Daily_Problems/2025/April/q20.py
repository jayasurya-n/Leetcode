from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hash = defaultdict(int)
        for num in answers:hash[num]+=1
        
        ans = 0
        for k in hash.keys():
            ans+=math.ceil(hash[k]/(k+1))*(k+1)
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))