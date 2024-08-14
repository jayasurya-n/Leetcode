from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int):
        n = len(nums)
        nums.sort()
        low,high = 0,nums[-1]-nums[0]
        
        # counts pairs with distance d
        def countPairs(d):
            i,j = 0,0
            cnt = 0
            while(j<n):
                while(nums[j]-nums[i]>d):i+=1
                cnt+=j-i
                j+=1
            return cnt
                
                
        while(low<high):
            mid = (low+high)//2
            if(countPairs(mid)<k):low=mid+1
            else:high = mid
        
        return low


# time complexity: O(nlogn+nlogM), M is max distance
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))