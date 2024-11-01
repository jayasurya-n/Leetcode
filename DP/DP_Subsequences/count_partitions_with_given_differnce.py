from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def countPartitions(self, n : int, d : int, arr : List[int]) -> int:
        total = (sum(arr)+d)//2
        if(2*total!=sum(arr)+d):return 0
        dp = [[0]*(total+1) for _ in range(n)]
        
        for i in range(n):dp[i][0] = 1
        if(arr[0]<=total):dp[0][arr[0]]+=1
        
        for i in range(1,n):
            for s in  range(0,total+1):
                dp[i][s] = dp[i-1][s]
                if(s>=arr[i]):dp[i][s]=(dp[i][s]+dp[i-1][s-arr[i]])%(10**9+7)
        return dp[n-1][total]
        
# time complexity: O(n*sum)
# space complexity: O(n*sum)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,d = list(map(int,input().strip().split()))
        arr = list(map(int,input().strip().split()))
        print(Solution().countPartitions(n,d,arr))