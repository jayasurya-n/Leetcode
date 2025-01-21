from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def evenlyDivides(self, n):
        temp = n
        ans = 0
        while(temp!=0):
            digit = temp%10
            if(digit!=0 and n%digit==0):ans+=1
            temp//=10
        return ans
        
# time complexity: O(logn)
# space complexity: O(logn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))