from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9+7
        mat = [[0]*26 for _ in range(26)]
        
        for i in range(26):
            for j in range(1,nums[i]+1):
                mat[(i+j)%26][i] = 1
        
        def matrix_mul(a,b):
            n = len(a)
            ans = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        ans[i][j]+=a[i][k]*b[k][j]
                        ans[i][j]%=mod
            return ans
        
        def power(matrix,b):
            n = len(matrix)
            ans = [[int(i==j) for j in range(n)] for i in range(n)]
            while b:
                if(b%2):ans = matrix_mul(ans,matrix)
                matrix = matrix_mul(matrix,matrix)
                b>>=1
            return ans
        
        mat = power(mat,t)     
        freq = [0]*26
        for ch in s:freq[ord(ch)-97]+=1
        
        ans = 0
        for i in range(26):
            for j in range(26):
                ans+=mat[i][j]*freq[j]
                ans%=mod
        return ans
        
# time complexity: O(n+logt*26^3)
# space complexity: O(26^2)
if __name__ == "__main__":
    for _ in range(ii()):
        s = si()
        t = ii()
        nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
        print(Solution().lengthAfterTransformations(s,t,nums))