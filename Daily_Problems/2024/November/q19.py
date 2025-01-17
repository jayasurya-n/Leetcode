from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i,j = 0,0
        hash = set()
        ans,sum = 0,0
        while(j<n):
            while(i<j and (nums[j] in hash or j-i+1>k)):
                sum-=nums[i]
                hash.remove(nums[i])
                i+=1
            
            sum+=nums[j]
            hash.add(nums[j])
            
            if(j-i+1==k):ans = max(ans,sum)
            j+=1
        return ans
            
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        k = int(input().strip())
        nums = list(map(int,input().strip().split()))
        print(Solution().maximumSubarraySum(nums,k))