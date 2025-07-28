from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # n = len(nums)
        # max_or = 0
        # for i in range(n):
        #     max_or|=nums[i]
        
        # cnt = 0 
        # for mask in range(1<<n):
        #     or_val = 0
        #     for i in range(n):
        #         if (mask>>i)&1==1:
        #             or_val|=nums[i]
            
        #     if(or_val==max_or):cnt+=1

        # return cnt

        n = len(nums)
        max_or = 0
        for i in range(n):
            max_or|=nums[i]
        
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(n):
            temp = defaultdict(int)
            for or_val in dp.keys():
                temp[or_val|nums[i]]+=dp[or_val]
            
            for or_val in temp.keys():
                dp[or_val]+=temp[or_val]
        
        return dp[max_or]

# time complexity: O(n*2**n),O(n*maxOR)
# space complexity: O(1),O(maxOR)
if __name__ == "__main__":
    for _ in range(ii()):
        nums = lii()
        print(Solution().countMaxOrSubsets(nums))