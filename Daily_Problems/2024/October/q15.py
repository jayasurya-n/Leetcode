from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def minimumSteps(self, s: str) -> int:
        # j = len(s)-1
        # while(j>=0 and s[j]!='0'):j-=1
        # steps = 0
        
        # for i in range(len(s)-1,-1,-1):
        #     if(s[i]=='1' and i<j):
        #         steps+=j-i
        #         j-=1
        # return steps
        
        white = 0
        steps = 0
        for cur in range(len(s)):
            if(s[cur]=='0'):
                steps+=cur-white
                white+=1
        return steps

# time complexity: O(n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))