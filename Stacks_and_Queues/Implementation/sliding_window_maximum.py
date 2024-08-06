from typing import List,Optional
from collections import deque
import sys
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int):
        q = deque()
        ans = []
        
        i,j = 0,0
        while(j<len(nums)):
            while(j-i+1>k):
                if(q[0]<=i):q.popleft()
                i+=1
            while(q and nums[q[-1]]<nums[j]):q.pop()
            q.append(j)
            if(j-i+1==k):ans.append(nums[q[0]])
            j+=1
        return ans

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        k = int(input().strip())
        print(Solution().maxSlidingWindow(nums,k))