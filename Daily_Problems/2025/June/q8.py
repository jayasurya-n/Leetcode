from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # stack = [0]
        
        # ans = []
        # while stack:
        #     ele = stack.pop()
        #     if(1<=ele<=n):ans.append(ele)
        #     for digit in range(9,-1,-1):
        #         new_ele = ele*10+digit
        #         if(1<=new_ele<=n):
        #             stack.append(new_ele)
        # return ans

        # def rec(num,ans):
        #     if(num>n):return
        #     ans.append(num)
        #     for digit in range(0,10):
        #         rec(num*10+digit,ans)
        
        # ans = []
        # for start in range(1,10):rec(start,ans)
        # return ans
    
        ans = []
        curr = 1
        for _ in range(n):
            ans.append(curr)
            if(curr*10<=n):curr*=10
            else:
                while curr%10==9 or curr>=n:curr//=10
                curr+=1
        return ans
                
# time complexity: O(n),O(n),O(n)
# space complexity: O(n),O(logn),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))