from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(deque)
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        
        for a,b in pairs:
            graph[a].append(b)
            outdegree[a]+=1
            indegree[b]+=1
        
        start = pairs[0][0]
        for node in graph:
            if(indegree[node]<outdegree[node]):start = node
        
        stack = [start]
        path = []
        
        while stack:
            while graph[stack[-1]]:
                next = graph[stack[-1]].popleft()
                stack.append(next)
            path.append(stack.pop())
        
        path.reverse()
        return [[path[i],path[i+1]] for i in range(len(path)-1)]
                
# time complexity: O(e)
# space complexity: O(v+e)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))