from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = deque()
        ans = [-1]*(n-k+1)
        
        for j in range(n):
            while q and q[0]<j-k+1:q.popleft()
            if(q and nums[q[-1]]+1!=nums[j]):q.clear()
            q.append(j)
            if(j>=k-1):ans[j-k+1] = nums[q[-1]] if len(q)==k else -1
        
        return ans
            
# time complexity: O(n)
# space complexity: O(k)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))