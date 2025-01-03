from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        bool = [0]*len(nums)
        for i in range(1,len(nums)):
            if(nums[i]%2==nums[i-1]%2):bool[i]=bool[i-1]+1
            else:bool[i]=bool[i-1]
        
        ans = []
        for i,j in queries:
            ans.append(bool[j]-bool[i]==0)
        return ans

# time complexity: O(n+q)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))