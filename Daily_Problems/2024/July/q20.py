from typing import List,Optional
import sys
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        matrix = [[0]*n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = min(rowSum[i],colSum[j])
                rowSum[i]-=matrix[i][j]
                colSum[j]-=matrix[i][j]
        return matrix


# time complexity: O(m*n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))