from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        m = int(math.sqrt(n))
        blocks = math.ceil(n/m)

        maxBlock = [0]*blocks
        maxi = 0
        for i in range(0,n):
            if(i!=0 and i%m==0):
                maxBlock[(i//m)-1] = maxi
                maxi = 0
            maxi = max(maxi,baskets[i])
        
        maxBlock[blocks-1] = maxi

        cnt = n
        for i in range(n):
            for j in range(blocks):
                if(maxBlock[j]>=fruits[i]):
                    for k in range(j*m,min(j*m+m,n)):
                        if(baskets[k]>=fruits[i]):
                            baskets[k] = 0
                            cnt-=1
                            break
                    
                    maxBlock[j] = max(baskets[j*m:min(j*m+m,n)])
                    break        
        return cnt

# time complexity: O(n*n(0.5))
# space complexity: O(n**(0.5))
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))