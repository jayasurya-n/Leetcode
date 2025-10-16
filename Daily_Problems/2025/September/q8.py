from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for a in range(1,n):
            b = n-a
            
            ok = True
            t1,t2 = a,b
            while a:
                dig = a%10
                if(dig==0):
                    ok = False
                    break
                a//=10
            
            while b:
                dig = b%10
                if(dig==0):
                    ok = False
                    break
                b//=10
            
            if(ok):return [t1,t2]

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))