from typing import List,Optional
from collections import deque
import sys
class Solution:
    def sumSubarrayMins(self, arr: List[int]):
        n = len(arr)
        mod = 10**9+7
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

         
        ans = 0
        for i in range(n):
            l = i-pse[i]
            r = nse[i]-i
            ans = (ans+(l*r*arr[i])%mod)%mod
        return ans
        
        
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().sumSubarrayMins(arr))