from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, functools

class Solution:
    # def largestNumber(self, nums: List[int]) -> str:
    #     def comparator(x,y):
    #         return str(x)+str(y)>=str(y)+str(x)
        
    #     def merge(l,mid,r,nums):
    #         temp = []
    #         i,j = l,mid+1
    #         while(i<=mid and j<=r):
    #             if(comparator(nums[i],nums[j])):
    #                 temp.append(nums[i])
    #                 i+=1
    #             else:
    #                 temp.append(nums[j])
    #                 j+=1
            
    #         while(i<=mid):
    #             temp.append(nums[i])
    #             i+=1
            
    #         while(j<=r):
    #             temp.append(nums[j])
    #             j+=1
                
    #         for k in range(len(temp)):
    #             nums[l+k] = temp[k]

    #     def mergeSort(l,r,nums):
    #         if(l>=r):return 
    #         mid = (l+r)//2
    #         mergeSort(l,mid,nums)
    #         mergeSort(mid+1,r,nums)
    #         merge(l,mid,r,nums)
        
    #     nums = list(map(str,nums))
    #     mergeSort(0,len(nums)-1,nums)
    #     ans = "".join(nums)
    #     if(ans[0]=='0'):return '0'
    #     return ans
    
    def largestNumber(self, nums: List[int]) -> str:
        def comparator(x,y):
            return -1 if x+y>=y+x else 1
        
        nums = list(map(str,nums))
        nums.sort(key=functools.cmp_to_key(comparator))
        ans = "".join(nums)
        if(ans[0]=='0'):return '0'
        return ans
        
# time complexity: O(nlogn),O(nlogn)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        nums = list(map(int,input().strip().split()))
        print(Solution().largestNumber(nums))