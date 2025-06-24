from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        # n = len(nums)
        # cnt = 0
        # # i-k to i+k
        # for i in range(min(k+1,n)):
        #     if(nums[i]==key):cnt+=1

        # ans = []
        # for i in range(n):
        #     if(cnt>0):ans.append(i)
        #     if(i-k>=0 and nums[i-k]==key):cnt-=1
        #     if(i+k+1<n and nums[i+k+1]==key):cnt+=1
        # return ans

        n = len(nums)
        right = 0
        ans = []
        for i in range(n):
            if(nums[i]==key):
                left = max(right,i-k)
                right = min(n-1,i+k)+1
                for ind in range(left,right):
                    ans.append(ind)
        return ans

# time complexity: O(n+k),O(n)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))