from typing import List,Optional
from collections import deque
import sys
class Solution:
    
    def maxMinWindow(self,arr,n):
        nse = [0]*n
        stack = []
        for i in range(n-1,-1,-1):
            while(stack and arr[stack[-1]]>=arr[i]):stack.pop()
            if(stack==[]):nse[i] = n
            else:nse[i] = stack[-1]
            stack.append(i)
        
        pse = [0]*n
        stack = []
        for i in range(0,n):
            while(stack and arr[stack[-1]]>=arr[i]):stack.pop()
            if(stack==[]):pse[i] = -1
            else:pse[i] = stack[-1]
            stack.append(i)
        
        ans = [-sys.maxsize]*(n+1)
        for i in range(n):
            size = nse[i]-pse[i]-1
            ans[size] = max(ans[size],arr[i])
        
        for i in range(n-1,0,-1):
            ans[i] = max(ans[i],ans[i+1])
        
        return ans[1:]

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        nums = list(map(int,input().strip().split()))
        print(Solution().maxMinWindow(nums,n))