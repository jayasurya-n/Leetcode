from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def checkValidString(self, s: str) -> bool:
        # stack = []
        # asteriks = []
        
        # for i,ch in enumerate(s):
        #     if(ch=='('):stack.append(i)
        #     elif(ch=='*'):asteriks.append(i)
        #     else:
        #         if(stack):stack.pop()
        #         elif(asteriks):asteriks.pop()
        #         else:return False
        
        # while stack and asteriks:
        #     if(stack.pop()>asteriks.pop()):return False
        # return not stack
        
        open = close = 0
        for i in range(len(s)):
            ch1,ch2 = s[i],s[len(s)-1-i]
            if(ch1=='(' or ch1=='*'):open+=1
            else:open-=1
            
            if(ch2==')' or ch2=='*'):close+=1
            else:close-=1
            
            if(open<0 or close<0):return False
        return True

# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))