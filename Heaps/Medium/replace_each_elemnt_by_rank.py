from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def replaceWithRank(self, n, arr):
        list = []
        for i,ele in enumerate(arr):list.append((ele,i))
        list.sort()
        
        ans = [0]*n
        ans[list[0][1]] = 1
        rank = 1
        for i in range(1,n):
            if(list[i][0]!=list[i-1][0]):rank+=1
            ans[list[i][1]] = rank
        return ans

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))