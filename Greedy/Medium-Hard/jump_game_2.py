from typing import List
import sys
class Solution:
    def jump(self, nums: List[int]) -> int:
        if(len(nums)==1):return 0
        
        maxReach = 0
        lastIndex = 0
        jumps = 0

        for i in range(len(nums)-1):
            maxReach = max(maxReach,i+nums[i])
            if(i==lastIndex):
                if(maxReach==i):return -1
                jumps+=1
                lastIndex = maxReach
        return jumps

# time complexity: O(n) 
# space complexity: O(1) 
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        print(Solution().jump(nums))