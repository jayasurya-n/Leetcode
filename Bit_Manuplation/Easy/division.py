from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:        
        sign = 1 if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else -1
        n = abs(dividend)
        d = abs(divisor)
        
        q = 0
        while(n>=d):
            i = 0
            while(d<<(i+1)<=n):i+=1
            q+=(1<<i)
            n-=d<<i

        if(q>=(1<<31)):
            if(sign==1):return (1<<31)-1
            else:return -(1<<31)
        return q*sign

# time complexity: O((logn)^2)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))