from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hash = defaultdict(int)
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):hash[nums[i]*nums[j]]+=1

        ans = 0
        for _,val in hash.items():
            if(val>1):ans+=(val)*(val-1)*4
        return ans

# time complexity: O(n^2)
# space complexity: O(n^2)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))