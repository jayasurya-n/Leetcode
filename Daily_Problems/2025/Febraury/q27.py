from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        # n = len(arr)
        # hash = defaultdict(int)
        # for id,num in enumerate(arr):hash[num]=id
        
        # dp = [[0]*n for _ in range(n)]
        # ans = 0
        # for j in range(1,n):
        #     for i in range(j):
        #         diff = arr[j]-arr[i]
        #         if(diff<arr[i] and diff in hash):
        #             id = hash[diff]
        #             dp[i][j] = dp[id][i]+1
        #         else:dp[i][j] = 2
        #         ans = max(ans,dp[i][j])
        # return ans if ans>=3 else 0
        
        n = len(arr)
        dp = [[0]*n for _ in range(n)]
        ans = 0
        for k in range(2,n):
            i,j = 0,k-1
            while(i<j):
                if(arr[i]+arr[j]==arr[k]):
                    dp[j][k] = dp[i][j]+1
                    ans = max(ans,dp[j][k])
                    i+=1
                    j-=1
                elif(arr[i]+arr[j]<arr[k]):i+=1
                elif(arr[i]+arr[j]>arr[k]):j-=1
        return ans+2 if ans else 0

# time complexity: O(n^2),O(n^2)
# space complexity: O(n^2),O(n^2)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))