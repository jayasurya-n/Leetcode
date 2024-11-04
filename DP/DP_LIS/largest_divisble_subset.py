from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        dp = [1]*n
        parent = [-1]*n
        for i in range(1,n):
            for j in range(i):
                if(nums[i]%nums[j]==0 and dp[i]<1+dp[j]):
                    dp[i] = 1+dp[j]
                    parent[i] = j
        
        ans = []
        ind = dp.index(max(dp))
        
        while ind!=-1:
            ans.append(nums[ind])
            ind = parent[ind]
        return ans[::-1]

# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))