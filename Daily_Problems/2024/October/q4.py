from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans = 0
        i,j = 0,len(skill)-1
        sum = skill[0]+skill[-1]
        while(i<j):
            if(skill[i]+skill[j]!=sum):return -1
            ans+=skill[i]*skill[j]
            i+=1
            j-=1
        return ans
            
# time complexity: O(nlogn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))