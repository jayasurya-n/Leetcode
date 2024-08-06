from typing import List,Optional
from collections import deque
import sys
class Solution:
    def minSwaps(self, nums: List[int]):
        n = len(nums)
        ones = sum([x for x in nums if x==1])
        
        swaps = 0 
        ans = n
        
        i,j = 0,0
        while(j<2*n):
            while(j-i+1>ones):
                if(nums[i%n]==0):swaps-=1
                i+=1
            if(nums[j%n]==0):swaps+=1
            if(j-i+1==ones):ans = min(ans,swaps)
            j+=1
        return ans
            
# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))