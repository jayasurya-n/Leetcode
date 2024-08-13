from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        
        ans,l = [],[]
        index = 0
        def findCombinations(index,sum):
            if(sum==target):
                ans.append(l[:])
                return 

            for i in range(index,n):
                if(i>index and candidates[i]==candidates[i-1]):continue
                if(candidates[i]+sum<=target):
                    l.append(candidates[i])
                    findCombinations(i+1,sum+candidates[i])
                    l.pop()
        
        findCombinations(0,0)
        return ans
                

# time complexity: O(2^n * k(average length of combination))
# space complexity: O(k*total combinations)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        candidates = list(map(int,input().strip().split()))
        target = int(input().strip())
        print(Solution().combinationSum2(candidates,target))