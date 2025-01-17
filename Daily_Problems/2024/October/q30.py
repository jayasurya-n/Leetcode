from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        
        for i in range(1,n):
            for prev in range(0,i):
                if(nums[i]>nums[prev]):lis[i] = max(lis[i],lis[prev]+1)
        
        lds = [1]*n
        for i in range(n-2,-1,-1):
            for prev in range(i+1,n):
                if(nums[i]>nums[prev]):lds[i] = max(lds[i],lds[prev]+1)
        
        ans = 0
        for i in range(n):
            if(lis[i]>1 and lds[i]>1):
                ans = max(ans,lis[i]+lds[i]-1)
        
        return n-ans

# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))