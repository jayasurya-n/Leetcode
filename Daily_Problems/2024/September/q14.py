from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxi = max(nums)
        ans,cnt = 0,0
        for i in range(len(nums)):
            if(nums[i]!=maxi):cnt=0
            else:
                cnt+=1
                ans = max(ans,cnt)
        return ans
                
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))