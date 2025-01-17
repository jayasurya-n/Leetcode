from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # ans = x
        # for i in range(n-1):
        #     ans = (ans+1)|x
        # return ans
        
        result = x
        n -= 1 
        mask = 1
        while n > 0:
            if (mask & x) == 0:
                result |= (n & 1) * mask
                n >>= 1
            mask <<= 1
        return result

# time complexity: O(n),O(logn)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))