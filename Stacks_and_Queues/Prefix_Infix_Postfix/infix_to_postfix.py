from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def minJumps(self, arr):
        if(arr[0]==0):return -1
        maxReach = arr[0] 
        steps = arr[0]
        jumps = 1
        
        for i in range(1,len(arr)-1):
            maxReach = max(maxReach,i+arr[i])
            steps-=1
            if(steps==0):
                jumps+=1
                steps = maxReach-i
                if(steps<=0):return -1
        return jumps

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))