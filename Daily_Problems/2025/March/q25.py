from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # xpairs = []
        # ypairs = []
        
        # for sx,sy,ex,ey in rectangles:
        #     xpairs.append((sx,ex))
        #     ypairs.append((sy,ey))

        # xpairs.sort(key=lambda x:x[0])
        # ypairs.sort(key=lambda x:x[0])
        
        # cnt1 = cnt2 = 0
        # pxend,pyend = xpairs[0][1],ypairs[0][1] 
        # for i in range(1,len(xpairs)):
        #     if(xpairs[i][0]>=pxend):
        #         cnt1+=1
        #         pxend = xpairs[i][1]
        #     else:pxend = max(pxend,xpairs[i][1])

        #     if(ypairs[i][0]>=pyend):
        #         cnt2+=1
        #         pyend = ypairs[i][1]
        #     else:pyend = max(pyend,ypairs[i][1])

        # return True if (cnt1>=2 or cnt2>=2) else False
        
        x_dict = defaultdict(int)
        y_dict = defaultdict(int)
        
        for sx,sy,ex,ey in rectangles:
            x_dict[sx]+=1
            x_dict[ex-1]-=1

            y_dict[sy]+=1
            y_dict[ey-1]-=1
        
        x_dict = sorted(x_dict.items(),key=lambda x:x[0])
        y_dict = sorted(y_dict.items(),key=lambda x:x[0])
        
        cnt1 = 0
        x_curr = 0
        for i in range(len(x_dict)):
            x_curr+=x_dict[i][1]            
            if(x_curr==0):cnt1+=1   
        
        cnt2 = 0
        y_curr = 0
        for i in range(len(y_dict)):
            y_curr+=y_dict[i][1]         
            if(y_curr==0):cnt2+=1
        
        return True if (cnt1>=2 or cnt2>=2) else False

# time complexity: O(nlogn),O(nlogn)
# space complexity: O(n),O(n)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))