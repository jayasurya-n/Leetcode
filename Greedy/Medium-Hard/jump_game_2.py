from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def jump(self, nums: List[int]) -> int:
        if(len(nums)==1):return 0
        if(nums[0]==0):return -1
        maxReach = nums[0] 
        steps = nums[0]
        jumps = 1
        
        for i in range(1,len(nums)-1):
            maxReach = max(maxReach,i+nums[i])
            steps-=1
            if(steps==0):
                jumps+=1
                steps = maxReach-i
                if(steps<=0):return -1
        return jumps

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        print(Solution().jump(nums))