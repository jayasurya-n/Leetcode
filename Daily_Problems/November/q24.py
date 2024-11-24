from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        smallest = sys.maxsize
        zeroes = False
        cnt,sum = 0,0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                curr = matrix[i][j]
                if(curr==0):zeroes=True
                if(curr<0):cnt+=1
                smallest = min(smallest,abs(curr))
                sum+=abs(curr)
        
        if(zeroes or cnt%2==0):return sum
        else:return sum-2*abs(smallest)
                
# time complexity: O(mn)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))