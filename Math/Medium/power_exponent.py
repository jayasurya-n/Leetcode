from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if(n<0):x = 1/x
        n=abs(n)
        while n>0:
            if(n&1):ans*=x
            x*=x
            n>>=1
        return ans

# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))