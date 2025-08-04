from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        hash = defaultdict(int)
        
        ans = left = 0
        for right in range(n):
            hash[fruits[right]]+=1

            while left<right and len(hash)>2:
                hash[fruits[left]]-=1
                if(hash[fruits[left]]==0):hash.pop(fruits[left])
                left+=1
            ans = max(ans,right-left+1)
        return ans 
    
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))