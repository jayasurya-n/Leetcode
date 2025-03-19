from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-2):
            if(nums[i]==1):continue
            for j in range(i,i+3):nums[j]^=1
            ans+=1
        
        for i in range(n-2,n):
            if(nums[i]==0):return -1
        
        return ans
        
# time complexity: O(n)
# space complexity: O(1)

# Hard Version Solution

        # n = len(nums)
        # count = [0]*n
        # ans = 0
        # csum = 0
        # for i in range(n-k+1):
        #     csum+=count[i]
        #     if(csum+nums[i])%2==1:continue
        #     count[i]+=1
        #     if(i+k<n):count[i+k]-=1
        #     csum+=1
        #     ans+=1
        
        # for i in range(n-k+1,n):
        #     csum+=count[i]
        #     if(nums[i]+csum)%2==0:return -1
        # return ans

        n = len(nums)
        q = deque([])
        ans = 0
        for i in range(n):
            if(i>=k):
                if(q and q[0]+k==i):q.popleft()
            
            if(len(q)%2==nums[i]):
                if(i+k>n):return -1
                ans+=1
                q.append(i)
        
        return ans
        
# time complexity: O(n),O(n)
# space complexity: O(n),O(k)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))