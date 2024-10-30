from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def isMaxHeap(self,arr,n):
        def check(i):
            if(i>=n):return 1
            l = 2*i+1
            r = 2*i+2
            if(l<n and arr[l]>arr[i]):return 0
            if(r<n and arr[r]>arr[i]):return 0
            return check(l) and check(r)
        return check(0)
                
# time complexity: O(n)
# space complexity: O(logn)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))