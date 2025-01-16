from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # if(len(s)%2==1):return False
        # open = 0
        # for i in range(len(s)):
        #     if(s[i]=='(' or locked[i]=='0'):open+=1
        #     else:open-=1
        #     if(open<0):return False
        
        # closed = 0
        # for i in range(len(s)-1,-1,-1):
        #     if(s[i]==')' or locked[i]=='0'):closed+=1
        #     else:closed-=1
        #     if(closed<0):return False
        # return True
        
        if(len(s)%2==1):return False
        stack = []
        unlocked = []
        for i,ch in enumerate(s):
            if(ch=='(' and locked[i]=='1'):stack.append(i)
            elif(locked[i]=='0'):unlocked.append(i)
            else:
                if(stack):stack.pop()
                elif(unlocked):unlocked.pop()
                else:return False
        
        while stack and unlocked and stack[-1]<unlocked[-1]:
            stack.pop()
            unlocked.pop()
        
        return not stack
        
# time complexity: O(n),O(n)
# space complexity: O(1),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))