from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        # n = len(nums)
        # def check(k):
        #     diff = [0]*n
        #     for i in range(k):
        #         l,r,val = queries[i]
        #         diff[l]-=val
        #         if(r+1<n):diff[r+1]+=val
            
        #     csum = 0
        #     for i in range(n):
        #         csum+=diff[i]
        #         if(csum+nums[i]>0):return False
        #     return True
        
        # low,high = 0,len(queries)
        # while(low<=high):
        #     mid = (low+high)>>1
        #     if(check(mid)):high = mid-1
        #     else:low = mid+1
        # return low if low<=len(queries) else -1 
        
        n = len(nums)
        tsum = 0
        k = 0
        diff = [0]*n
        
        for i in range(n):
            while(tsum+diff[i]+nums[i]>0):
                k+=1
                if(k>len(queries)):return -1
                
                l,r,val = queries[k-1]
                if(r>=i):
                    diff[max(l,i)]-=val
                    if(r+1<n):diff[r+1]+=val
            tsum+=diff[i]
        return k

# time complexity: O((m+n)logm), O(m+n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))