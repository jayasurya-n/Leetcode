from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # hash = set()
        # while n>0:
        #     b=0
        #     while(3**b<=n):b+=1
        #     b-=1
        #     if(b in hash):return False
        #     hash.add(b)
        #     n-=3**b
        # return True

        pb = -1
        while n>0:
            b=0
            while(3**b<=n):b+=1
            b-=1
            if(b==pb):return False
            pb=b
            n-=3**b
        return True

# time complexity: O(logn_3),O(logn_3)
# space complexity: O(logn_3),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))