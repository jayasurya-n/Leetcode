from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # n = len(pattern)
        # def rec(digits,temp):
        #     if(len(temp)==n+1):return "".join(temp)
            
        #     for i in range(len(digits)):
        #         if(not digits[i]):continue
        #         l = len(temp)
        #         if(l==0  or 
        #            (pattern[l-1]=='I' and i+1>int(temp[-1])) or 
        #            (pattern[l-1]=='D' and i+1<int(temp[-1]))):
        #             temp.append(str(i+1))
        #             digits[i] = False
        #             ans = rec(digits,temp)
        #             if(ans):return ans
        #             digits[i] = True
        #             temp.pop()
        #     return None
        
        # digits = [True]*9
        # return rec(digits,[])
        
        # val = 1
        # stack = []
        # ans = []
        # for i in range(len(pattern)):
        #     stack.append(str(val))
        #     val+=1
        #     if(pattern[i]=='I'):
        #         while(stack):ans.append(stack.pop())
        
        # stack.append(str(val))
        # while(stack):ans.append(stack.pop())
        # return "".join(ans)
        
        n = len(pattern)
        ans = ['0']*(n+1)
        def rec(i,cnt):
            if(i==n):
                ans[i] = str(cnt)
                return cnt+1
            
            if(pattern[i]=='I'):
                ans[i] = str(cnt)
                rec(i+1,i+2)
            else:
                cnt = rec(i+1,cnt)
                ans[i] = str(cnt)
            return cnt+1

        rec(0,1)
        return "".join(ans)

# time complexity: O((n+1)*(n+1)!),O(n),O(n)
# space complexity: O(n),O(n),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        s = si()
        print(Solution().smallestNumber(s))