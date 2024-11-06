from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        cmaxi,cmini = nums[0],nums[0]
        pmaxi = -sys.maxsize
        curr = bin(nums[0]).count('1')
        for i in range(1,len(nums)):
            if(curr==bin(nums[i]).count('1')):
                cmaxi = max(cmaxi,nums[i])
                cmini = min(cmini,nums[i])
            else:
                if(pmaxi>cmini):return False
                pmaxi = cmaxi
                cmaxi,cmini = nums[i],nums[i]
                curr = bin(nums[i]).count('1') 
        return pmaxi<cmini
    
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))