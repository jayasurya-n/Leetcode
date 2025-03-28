from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # n = len(nums)
        # hash = defaultdict(int)
        # for num in nums:hash[num]+=1
        
        # major = None
        # for num in hash.keys():
        #     if(hash[num]>n//2):major = num
        
        # if(not major):return -1
        
        # cnt = 0
        # for i in range(n):
        #     if(nums[i]==major):cnt+=1
        #     if(cnt>(i+1)//2 and (hash[major]-cnt)>(n-i-1)//2):return i
        # return -1    


        n = len(nums)
        major = nums[0]
        cnt = 0
        for num in nums:
            if(cnt==0):major = num
            if(num==major):cnt+=1
            else:cnt-=1
        
        major_cnt = nums.count(major)     
        if(major_cnt<=n//2):return -1
    
        cnt = 0
        for i in range(n):
            if(nums[i]==major):cnt+=1
            if(cnt>(i+1)//2 and (major_cnt-cnt)>(n-i-1)//2):return i
        return -1 

# time complexity: O(n),O(n)
# space complexity: O(n),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))