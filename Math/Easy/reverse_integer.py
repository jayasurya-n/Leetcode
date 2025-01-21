from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x>0 else -1
        ans = 0
        x = abs(x)
        while(x!=0):
            digit = x%10
            ans = ans*10+digit
            if(sign==1 and ans>=(1<<31)):return 0
            if(sign==-1 and ans>(1<<31)):return 0
            x//=10
        return ans*sign

# time complexity: O(logn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))