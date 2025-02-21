from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # n = len(nums)
        # hash = [False]*n
        
        # for string in nums:
        #     val = 0
        #     for i,ch in enumerate(string):
        #         if(ch=='1'):val+=1<<(n-1-i)
        #     if(val<n):hash[val] = True
        
        # mex = 0
        # while(mex<n and hash[mex]):mex+=1
        # ans = []
        # for i in range(n-1,-1,-1):
        #     ans.append(str((mex>>i)&1))
        # return "".join(ans)
        
        n = len(nums)
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append('1' if curr=='0' else '0')
        return "".join(ans)
    
# time complexity: O(n^2),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))