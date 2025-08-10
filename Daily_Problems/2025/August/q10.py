from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # power2digits = []
        # curr = 1
        # for i in range(31):
        #     temp = curr
        #     digits = []
        #     while temp:
        #         digits.append(temp%10)
        #         temp//=10
        #     power2digits.append(sorted(digits))
        #     curr*=2
        
        # digits = []
        # while n:
        #     digits.append(n%10)
        #     n//=10
        # digits.sort()

        # for i in range(31):
        #     if(digits==power2digits[i]):return True
        
        # return False

        s = sorted(str(n))
        for i in range(31):
            if(s==sorted(str(1<<i))):
                return True
        return False

# time complexity: O(31*dlogd)
# space complexity: O(d)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))