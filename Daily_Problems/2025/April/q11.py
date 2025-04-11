from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low,high+1):
            s = str(num)
            n = len(s)
            if(n%2==1):continue
            sum, cnt = 0,1 
            while num:
                digit = num%10
                if(cnt<=n//2):sum+=digit
                else:sum-=digit
                num//=10
                cnt+=1
            if(sum==0):ans+=1
        return ans

# time complexity: O(n)
# space complexity: O(logn)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))