from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def bitManipulation(self, n, i):
        i-=1 #1-based to 0-based
        
        # get ith bit 
        print(1 if n&(1<<i)!=0 else 0)

        # set ith bit
        print("Set ith bit:", n|(1<<i))
        
        # clear ith bit
        print("Clear ith bit:", n&(~(1<<i)))
        
        # toggle ith bit
        print("Toggle ith bit:", n^(1<<i))
        
        # remove the (right-most)last set bit or least significant set bit
        print("remove last set bit:", n&(n-1))
        
        # check if a num is power of 2
        print("Is power of 2:", n&(n-1)==0)
        
        # odd check
        print("Is odd:", n&1==1)
        
        # swap two numbers a,b
        a,b = 2,7
        a = a^b
        b = a^b
        a = a^b
        print("Swap a,b:", a,b)
        
        # count set bits
        cnt = 0
        num = n
        while(num!=0):
            num&=(num-1)
            cnt+=1
        print("Total set bits-method1:", cnt)
        
        cnt = 0
        num = n
        while(num!=0):
            cnt+=(num&1)
            num>>=1
        print("Total set bits-method2:", cnt)
        
        
# time complexity: O(1)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n,i = list(map(int,input().strip().split()))
        print(Solution().bitManipulation(n,i))