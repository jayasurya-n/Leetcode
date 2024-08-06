from typing import List,Optional
from collections import deque
import sys
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int):
        subSums = []
        mod = 10**9+7
        for i in range(n):
            sum = 0
            for j in range(i,n):
                sum+=nums[j]
                subSums.append(sum)
        
        subSums.sort()
        
        ans = 0
        for i in range(left,right+1):
            ans=(ans+subSums[i-1])%mod
        return ans

# time complexity: O(n^2logn)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        l,r = list(map(int,input().strip().split()))
        print(Solution().rangeSum(arr,len(arr),l,r))