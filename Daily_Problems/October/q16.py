from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = [[a,'a'],[b,'b'],[c,'c']]
        ans = ""
        
        while True:
            counts.sort(reverse=True)
            added = False
            
            for i in range(3):
                count,char = counts[i]
                if(count==0):break
                if(len(ans)>=2 and ans[-1]==ans[-2]==char):continue
                
                ans+=char
                counts[i][0]-=1
                added = True
                break
            
            if(not added):break
        
        return ans

# time complexity: O(a+b+c)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))