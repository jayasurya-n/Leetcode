from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        pshift = [0]*n
        
        for start,end,dir in shifts:
            if(dir==1):
                pshift[start]+=1
                if(end<n-1):pshift[end+1]-=1
            else:
                pshift[start]-=1
                if(end<n-1):pshift[end+1]+=1
        
        for i in range(n):
            pshift[i]+=(pshift[i-1] if i>0 else 0)
        
        ans = []
        for i,ch in enumerate(s):
            value = (ord(ch)-ord('a')+pshift[i]+26)%26
            ans.append(chr(ord('a')+value))
        return "".join(ans)
            
# time complexity: O(n+m)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))