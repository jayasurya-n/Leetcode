from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # cnt = 0
        # ans = ""
        # def rec(temp):
        #     if(len(temp)==n):
        #         nonlocal cnt
        #         cnt+=1
        #         if(cnt==k):
        #             nonlocal ans
        #             ans = temp[:]
        #             return True
        #         return False

        #     for ch in ['a','b','c']:
        #         if(not temp or temp[-1]!=ch):
        #             temp.append(ch)
        #             if(rec(temp)):return True
        #             temp.pop()
        #     return False
        
        # rec([])
        # return "".join(ans)
        
        # cnt = 0
        # ans = ""
        # stack = [[]]
        
        # while stack:
        #     temp = stack.pop()
        #     if(len(temp)==n):
        #         cnt+=1
        #         if(cnt==k):return "".join(temp)
        #         continue
            
        #     for ch in ['c','b','a']:
        #         if(not temp or temp[-1]!=ch):
        #             new = temp[:]
        #             new.append(ch)
        #             stack.append(new)
                    
        # return ""
        
        if(k>3*(1<<(n-1))):return ""
        ans = ['a']*n
        
        if(k<=1<<(n-1)):
            ans[0] = 'a'
        elif(k<=2*(1<<(n-1))):
            ans[0] = 'b'
            k-=(1<<(n-1))
        else:
            ans[0] = 'c'
            k-=2*(1<<(n-1))
        
        for i in range(1,n):
            size = 1<<(n-i)
            if(k<=size//2):
                if(ans[i-1]=='a'):ans[i] = 'b'
                elif(ans[i-1]=='b'):ans[i] = 'a'
                elif(ans[i-1]=='c'):ans[i] = 'a'
            else:
                if(ans[i-1]=='a'):ans[i] = 'c'
                elif(ans[i-1]=='b'):ans[i] = 'c'
                elif(ans[i-1]=='c'):ans[i] = 'b'
                k-=size//2

        return "".join(ans)
                
# time complexity: O(k*n or 3n*2^(n-1)),O(k*n or 3n*2^(n-1)),O(n)
# space complexity: O(n),O(n^2),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n,k = lii()
        print(Solution().getHappyString(n,k))