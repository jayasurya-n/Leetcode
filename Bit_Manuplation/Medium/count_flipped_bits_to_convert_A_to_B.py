from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # if(goal>start):start,goal = goal,start
        
        # ans = 0
        # i = 0
        # while((1<<i)<=start):
        #     if((start>>i)&1!=(goal>>i)&1):ans+=1
        #     i+=1
        # return ans

        # xor = start^goal
        # ans = 0
        # while(xor!=0):
        #     xor&=(xor-1)
        #     ans+=1
        # return ans
        
        return (start^goal).bit_count()
    
# time complexity: O(log(max(m,n))),O(set bits),O(set bits)
# space complexity: O(1),O(1),O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))