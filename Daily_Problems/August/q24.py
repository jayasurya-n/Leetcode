from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def nearestPalindromic(self, n: str):
        l = len(n)
        half = int(n[:((l+1)//2)])
        
        def findPossibs(num,l):
            ans = num
            if(l%2==1):ans//=10
            while num>0:
                ans = ans*10 + num%10
                num//=10
            return ans 
        
        possibs = []
        possibs.append(findPossibs(half,l))
        possibs.append(findPossibs(half+1,l))
        possibs.append(findPossibs(half-1,l))
        possibs.append(10**(l-1)-1)
        possibs.append(10**(l)+1)
        
        print(possibs)
        ans = -1
        mini = sys.maxsize
        n = int(n)
        for i in range(len(possibs)):
            if(n==possibs[i]):continue
            if(abs(n-possibs[i])<mini):
                mini = abs(n-possibs[i])
                ans = possibs[i]
            elif(abs(n-possibs[i])==mini):
                ans = min(ans,possibs[i])
        return str(ans)
        

# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = input().strip()
        print(Solution().nearestPalindromic(n))