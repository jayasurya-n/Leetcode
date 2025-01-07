from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # last = days[-1]
        # dp = [0]*(last+1)
        
        # travelDays = set(days)
        # for i in range(1,last+1):
        #     if(i not in travelDays):dp[i] = dp[i-1]
        #     else:
        #         dp[i] = min(dp[i-1]+costs[0],
        #                     dp[max(0,i-7)]+costs[1],
        #                     dp[max(0,i-30)]+costs[2])
        # return dp[last]
        
        last = days[-1]
        dp = [0]*(last+1)
        
        ind = 0
        for i in range(1,last+1):
            if(i<days[ind]):dp[i] = dp[i-1]
            else:
                ind+=1
                dp[i] = min(dp[i-1]+costs[0],
                            dp[max(0,i-7)]+costs[1],
                            dp[max(0,i-30)]+costs[2])
        return dp[last]

# time complexity: O(last),O(last)
# space complexity: O(last+n),O(last)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))