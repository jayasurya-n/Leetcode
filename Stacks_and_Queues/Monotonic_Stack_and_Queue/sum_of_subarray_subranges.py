from typing import List,Optional
from collections import deque
import sys
class Solution:
    def subArrayRanges(self, nums: List[int]):
        n = len(arr)
        nse = [0]*n
        pse = [0]*n
        
        stack = []
        for i in range(n-1,-1,-1):
            while(stack and stack[-1][0]>arr[i]):stack.pop()
            if(stack==[]):nse[i] = n
            else:nse[i] = stack[-1][1]
            stack.append((arr[i],i))
        
        stack = []
        for i in range(0,n):
            while(stack and stack[-1][0]>=arr[i]):stack.pop()
            if(stack==[]):pse[i] = -1
            else:pse[i] = stack[-1][1]
            stack.append((arr[i],i))
        
        nge = [0]*n
        pge = [0]*n
        
        stack = []
        for i in range(n-1,-1,-1):
            while(stack and stack[-1][0]<arr[i]):stack.pop()
            if(stack==[]):nge[i] = n
            else:nge[i] = stack[-1][1]
            stack.append((arr[i],i))

        stack = []
        for i in range(0,n):
            while(stack and stack[-1][0]<=arr[i]):stack.pop()
            if(stack==[]):pge[i] = -1
            else:pge[i] = stack[-1][1]
            stack.append((arr[i],i))
         
        ans = 0
        for i in range(n):
            l1 = i-pge[i]
            r1 = nge[i]-i
            ans+= l1*r1*arr[i]
            
            l2 = i-pse[i]
            r2 = nse[i]-i
            ans-=l2*r2*arr[i]
        return ans
        
        
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().subArrayRanges(arr))