from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        hash = defaultdict(lambda:[-1,-1])
        
        def digitSum(n):
            csum = 0
            while(n>0):
                csum+=n%10
                n//=10
            return csum
        
        for num in nums:
            csum = digitSum(num) 
            temp = sorted([num,hash[csum][0],hash[csum][1]])
            hash[csum] = [temp[1],temp[2]]
        
        ans = -1
        for val in hash.values():
            if(val[0]!=-1 and val[1]!=-1):ans = max(ans,val[0]+val[1])
        return ans

# time complexity: O(nlogm)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))