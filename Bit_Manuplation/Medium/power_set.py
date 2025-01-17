from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        for cnt in range(0,(1<<n)):
            temp = []
            for i in range(n):
                if(cnt&(1<<i)!=0):temp.append(nums[i])
            ans.append(temp)
        return ans

# time complexity: O(n*2^n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))