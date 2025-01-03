from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        minheap = [(num,i) for i,num in enumerate(nums)]
        heapq.heapify(minheap)
        marked = [False]*n
        score = 0
        
        while minheap:
            while minheap and marked[minheap[0][1]]:heapq.heappop(minheap)
            if(not minheap):break
            num,i = heapq.heappop(minheap)

            score+=num
            marked[i] = True
            if(i>0):marked[i-1]=True
            if(i<n-1):marked[i+1]=True
        return score

# time complexity: O(nlogn)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        arr = list(map(int,input().strip().split()))
        print(Solution().findScore(arr))