from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        i,ans = 0,0
        maxq, minq = deque(),deque()
        for j,num in enumerate(nums):
            while maxq and nums[maxq[-1]]<=num:maxq.pop()
            maxq.append(j)
            
            while minq and nums[minq[-1]]>=num:minq.pop()
            minq.append(j)
            
            while nums[maxq[0]]-nums[minq[0]]>2:
                i+=1
                while maxq and maxq[0]<i:maxq.popleft()
                while minq and minq[0]<i:minq.popleft()
            
            ans+=j-i+1
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))