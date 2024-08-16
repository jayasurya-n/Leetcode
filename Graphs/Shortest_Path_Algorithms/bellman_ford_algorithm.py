from typing import List,Optional
from collections import deque
import sys, math, heapq

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    def bellman_ford(self, v, edges, s):
        distance = [10**8]*v
        distance[s] = 0
        
        for ite in range(v-1):
            for i in range(len(edges)):
                u,v,w = edges[i]
                if(distance[u]!=10**8 and w+distance[u]<distance[v]):
                    distance[v] = w+distance[u]
        
        for i in range(len(edges)):
                u,v,w = edges[i]
                if(distance[u]!=10**8 and w+distance[u]<distance[v]):
                    return [-1]
        
        return distance 

# time complexity: O(ve)
# space complexity: O(v)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))