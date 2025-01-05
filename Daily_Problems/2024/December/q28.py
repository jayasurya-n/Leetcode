from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        subarray_sums = [0]*(n-k+1)
        
        cur_sum = sum(nums[:k])
        subarray_sums[0] = cur_sum
        for i in range(k,n):
            cur_sum+=nums[i]-nums[i-k]
            subarray_sums[i-k+1] = cur_sum
        
        dp = [[0]*(4) for _ in range(n)]
        indices = [[-1]*(4) for _ in range(n)]
        
        for cnt in range(1,4):
            for i in range(k*cnt-1,n):
                dp[i][cnt] = dp[i-1][cnt]
                indices[i][cnt] = indices[i-1][cnt]
                
                if(dp[i-k][cnt-1]+subarray_sums[i-k+1]>dp[i][cnt]):
                    dp[i][cnt] = subarray_sums[i-k+1]+dp[i-k][cnt-1]
                    indices[i][cnt] = i-k+1
        
        ans = []
        i = n-1
        
        for cnt in range(3,0,-1):
            ind = indices[i][cnt]
            ans.append(ind)
            i = ind-1
        return ans[::-1] 
                
# time complexity: O(3n)
# space complexity: O(3n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))