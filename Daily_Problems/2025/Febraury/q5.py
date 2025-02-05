from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        cnt = 0
        i1 = i2 = -1
        for i,(ch1,ch2) in enumerate(zip(s1,s2)):
            if(ch1!=ch2):
                if(i1==-1):i1 = i
                else:i2 = i 
                cnt+=1
        
        if(cnt==1 or cnt>2):return False
        return (s1[i1]==s2[i2] and s1[i2]==s2[i1]) or cnt==0

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))