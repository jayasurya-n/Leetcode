from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # maxi = max(nums)
        # numerical = [0]*(maxi+1)
        
        # for ele in nums:
        #     s,e = ele-k,ele+k+1
        #     numerical[max(s,0)]+=1
        #     if(e<=maxi):numerical[e]-=1
        
        # ans,sum = 0,0
        # for val in numerical:
        #     sum+=val
        #     ans = max(ans,sum)
        # return ans

        # events = []
        # for ele in nums:
        #     events.append((ele-k,1))
        #     events.append((ele+k+1,-1))
        # events.sort()
        
        # ans,sum = 0,0
        # for _,val in events:
        #     sum+=val
        #     ans = max(ans,sum)
        # return ans
        
        # nums.sort()
        # ans,i = 0,0
        
        # for j in range(len(nums)):
        #     while nums[j]-nums[i]>2*k:i+=1
        #     ans = max(ans,j-i+1)
        # return ans
        
        nums.sort()
        ans = 0
        
        for i,ele in enumerate(nums):
            j = bisect.bisect_right(nums,ele+2*k)-1
            ans = max(ans,j-i+1)
        return ans
        
# time complexity: O(n+maxi),O(nlogn),O(nlogn),O(nlogn)
# space complexity: O(maxi),O(n),O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))