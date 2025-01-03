from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [0]*len(queries)
        new_queries = []
        for i,(x,y) in enumerate(queries):
            if(x>y):x,y = y,x
            if(x==y or heights[x]<heights[y]):ans[i] = y
            else:new_queries.append((y,i,x))
            
        new_queries.sort(key=lambda x:x[0],reverse=True)      
        
        n = len(heights)
        top = n-1
        stack = [] 
        for y,ind,x in new_queries:
            while(top>y):
                while stack and heights[stack[-1]]<heights[top]:stack.pop()
                stack.append(top)
                top-=1
            
            idx = bisect.bisect_right([heights[i] for i in reversed(stack)], heights[x])
            ans[ind] = stack[len(stack)-1-idx] if idx<len(stack) else -1
        return ans
                    
# time complexity: O(qlogq+qlogn+n)
# space complexity: O(q+n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))