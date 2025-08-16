from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def maximum69Number (self, num: int) -> int:
        # s = list(str(num))
        # ans = 0
        # flag = 1
        # for i in range(len(s)):
        #     if(flag and s[i]=='6'):
        #         s[i] = '9'
        #         break
        # return int("".join(s))

        ans = org = num
        val = 1
        while num:
            digit = num%10
            if(digit==6):
                temp = org+3*val
                ans = max(temp,ans)
            num//=10
            val*=10
        return ans

# time complexity: O(logn),O(logn)
# space complexity: O(logn),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))