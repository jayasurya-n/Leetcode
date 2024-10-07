from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def minLength(self, s: str) -> int:
    #     stack = []
    #     for ch in s:
    #         if(stack and stack[-1]=='A' and ch=='B'):stack.pop()
    #         elif(stack and stack[-1]=='C' and ch=='D'):stack.pop()
    #         else:stack.append(ch)
    #     return len(stack)
    def minLength(self, s: str) -> int:
        ls = list(s)
        i,j = 0,0
        while(j<len(ls)):
            ls[i] = ls[j]
            if((i>0 and ls[i-1]=='A' and ls[i]=='B') or 
               (i>0 and ls[i-1]=='C' and ls[i]=='D')):i-=1
            else:i+=1
            j+=1
        return i

# time complexity: O(n),O(n)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))