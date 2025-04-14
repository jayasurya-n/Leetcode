from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # n = len(arr)
        # ans = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if(abs(arr[j]-arr[i])<=a and 
        #                abs(arr[k]-arr[j])<=b and 
        #                abs(arr[k]-arr[i])<=c):ans+=1
        # return ans
        
        n = len(arr)
        count = [0]*1001
        ans = 0
        for j in range(n):
            for k in range(j+1,n):
                if(abs(arr[k]-arr[j])<=b):
                    l1,r1 = arr[j]-a,arr[j]+a
                    l2,r2 = arr[k]-c,arr[k]+c
                    l,r = max(0,l1,l2),min(1000,r1,r2)
                    if l<=r: ans+=count[r]-(count[l-1] if l>0 else 0)
            
            for k in range(arr[j],1001):count[k]+=1
        return ans    

# time complexity: O(n^3),O(n^2+n*S)
# space complexity: O(1),O(S)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))