from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        set_bits = bin(num2).count('1')
        ans = 0

        for i in range(31,-1,-1):
            if(set_bits>0 and (num1&(1<<i))):
                ans|=(1<<i)
                set_bits-=1
        
        for i in range(32):
            if(set_bits>0 and not (ans&(1<<i))):
                ans|=(1<<i)
                set_bits-=1
        return ans

# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))