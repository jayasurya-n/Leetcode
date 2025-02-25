from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # mod = 10**9+7
        # ans = csum = 0
        # even,odd = 1,0
        # for i in range(len(arr)):
        #     csum+=arr[i]
        #     if(csum%2==0):
        #         ans+=odd
        #         ans%=mod
        #         even+=1
        #     else:
        #         ans+=even
        #         ans%=mod
        #         odd+=1
        # return ans
        
        mod = 10**9+7
        dp = [[0,0] for _ in range(len(arr)+1)]
        csum = 0
        for i in range(1,len(arr)+1):
            if(arr[i-1]%2):
                dp[i][0] = dp[i-1][1]+1
                dp[i][0]%=mod
                dp[i][1] = dp[i-1][0]
            else:
                dp[i][1] = dp[i-1][1]+1
                dp[i][1]%=mod
                dp[i][0] = dp[i-1][0]
        
        ans = 0
        for i in range(1,len(arr)+1):
            ans+=dp[i][0]
            ans%=mod
        return ans   

# time complexity: O(n),O(n)
# space complexity: O(1),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))