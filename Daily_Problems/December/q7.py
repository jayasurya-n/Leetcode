from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        low,high = 1,max(nums)
        while(low<=high):
            mid = (low+high)//2
            ope = 0
            for balls in nums:ope+=math.ceil(balls/mid)-1
            if(ope<=maxOperations):high = mid-1
            else:low = mid+1
        return low 
            
# time complexity: O(nlogm)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))