from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def countSetBits(self,n):
        cnt,b = 0,0
        while((1<<b)<=n):
            block = 1<<(b+1)
            cnt+=(n//block)*(block>>1)
            
            rem = n%block
            # 1 is added beacuse the pattern occurs when 0 is inlcuded at start 
            cnt+=max(0,(rem-(1<<b)+1)) 
            b+=1
        return cnt
    
# time complexity: O(logn)
# space complexity: O(1)

if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))