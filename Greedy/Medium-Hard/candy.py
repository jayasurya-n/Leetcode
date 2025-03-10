from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1]*n
        
        for i in range(1,n):
            if(ratings[i]>ratings[i-1]):candies[i] = candies[i-1]+1
        
        for i in range(n-2,-1,-1):
            if(ratings[i]>ratings[i+1]):candies[i] = max(candies[i],candies[i+1]+1)
        
        return sum(candies)
                
# time complexity: O(n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))