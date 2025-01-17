from typing import List,Optional
import sys
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ans = []
        for i in range(0,len(matrix)):
            j = matrix[i].index(min(matrix[i]))
            maxi = -sys.maxsize
            for k in range(0,len(matrix)):
                maxi = max(maxi,matrix[k][j])
            if(matrix[i][j]==maxi):ans.append(maxi)
        return ans


# time complexity: O(m*n)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        m,n = list(map(int,input().strip().split()))
        matrix = [list(map(int,input().strip().split())) for _ in range(m)]
        print(Solution().func(arr,n))