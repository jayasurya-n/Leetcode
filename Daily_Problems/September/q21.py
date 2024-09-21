from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    # def lexicalOrder(self, n: int) -> List[int]:
    #     ans = []
    #     def genLexical(num):
    #         if(num>n):return
    #         ans.append(num)
    #         for d in range(0,10):
    #             genLexical(num*10+d)
                
    #     for i in range(1,10):genLexical(i)
    #     return ans
    
    def lexicalOrder(self, n: int) -> List[int]:
        num = 1
        ans = []
        for _ in range(n):
            ans.append(num)
            if(num*10<=n):num*=10
            else:
                if(num==n):num//=10
                num+=1
                while(num%10==0):num//=10
        return ans
                
# time complexity: O(n),O(n)
# space complexity: O(logn),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        print(Solution().lexicalOrder(n))