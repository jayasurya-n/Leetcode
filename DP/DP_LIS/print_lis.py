from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def longestIncreasingSubsequence(self, n,arr):
        dp = [1]*n
        parent = [-1]*n
        for i in range(1,n):
            for j in range(i):
                if(arr[j]<arr[i] and dp[i]<1+dp[j]):
                    dp[i] = 1+dp[j]
                    parent[i] = j
                    # no need of another if condiiton for 
                    # index-wise lexgraphic as we are looping from smallest index
        
        ind = dp.index(max(dp))
        ans = []
        while ind!=-1:
            ans.append(arr[ind])
            ind = parent[ind]
        return ans[::-1]
        
# time complexity: O(n^2)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))