from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # ans = up = down = 1
        
        # for i in range(len(nums)-1):
        #     if(nums[i]<nums[i+1]):up+=1
        #     else:up = 1
        #     ans = max(ans,up)

        # for i in range(len(nums)-1):
        #     if(nums[i]>nums[i+1]):down+=1
        #     else:down = 1
        #     ans = max(ans,down)
        # return ans
        
        ans = up = down = 1
        
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):
                up+=1
                down=1
            elif(nums[i]>nums[i+1]):
                down+=1
                up=1
            else:
                up=1
                down=1
            ans =  max(ans,up,down)
        return ans

# time complexity: O(n),O(n)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))