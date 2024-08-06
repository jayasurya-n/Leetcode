from typing import List
import sys
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # max_reach = 0
        # for i in range(len(nums)):
        #     if(i>max_reach):return False
        #     max_reach = max(max_reach,i+nums[i])
        # # return max_reach>=len(nums)-1
        # return True

        goal = len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if(nums[i]+i>=goal):
                goal = i
        print("Goal",goal)
        return goal==0

# time complexity: O(n) in both solutions
# space complexity: O(1) in both solutions
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = list(map(int,input().strip().split()))
        print(Solution().canJump(nums))