from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # even = defaultdict(int)
        # odd = defaultdict(int)
        # for num in digits:
        #     if(num%2):odd[num]+=1
        #     else:even[num]+=1
                
        # def rec(i,curr):
        #     if(i==3):
        #         self.ans.append(curr)
        #         return
            
        #     for d in even.keys():
        #         if(even[d]==0 or (i==0 and d==0)):continue
        #         even[d]-=1
        #         rec(i+1,10*curr+d)
        #         even[d]+=1

        #     if(i!=2):
        #         for d in odd.keys():
        #             if(odd[d]==0):continue
        #             odd[d]-=1
        #             rec(i+1,10*curr+d)
        #             odd[d]+=1
        
        # self.ans = []
        # rec(0,0)
        # return sorted(self.ans)
        
        hash = defaultdict(int)
        for num in digits:hash[num]+=1
        ans = []
        
        for num in range(100,1000):
            if(num%2):continue
            hash2 = defaultdict(int)
            for d in str(num):hash2[int(d)]+=1
            
            bool = True
            for d in hash2.keys():
                if(hash2[d]>hash[d]):bool = False
            if(bool):ans.append(num)
        
        return sorted(ans)
            
# time complexity: O(1),O(1)
# space complexity: O(1),O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        digits = lii()
        print(Solution().findEvenNumbers(digits))