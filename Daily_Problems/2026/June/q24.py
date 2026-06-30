from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        # dp0[i][x]: number of zizag arrays ending with x(decreasing) and length i+1, 
        # dp1[i][x]: number of zizag arrays ending with x(increasing) and lenght i+1
        
        # dp0[i] = dp1[i-1]*A (A:k*k), upper triangle matrix
        # dp1[i] = dp0[i-1]*B (B:k*k), lower triangle matrix
        # [dp0[i],dp1[i]] = [dp0[i-1],dp1[i-1]]*[[0,A],[B,0]]
        
        MOD = 10**9+7
        k = r-l+1

        U = [[0] * 2 * k for _ in range(2 * k)]
        for i in range(k):
            for j in range(i + 1, k):
                U[i][j + k] = 1
                
        for i in range(k):
            for j in range(i):
                U[i + k][j] = 1
        

        def matrix_mul(A,B):
            m,p,n = len(A),len(B),len(B[0])
            res = [[0]*n for _ in range(m)]

            for i in range(m):
                for k in range(p):
                    val = A[i][k]
                    if val == 0:
                        continue
                    
                    for j in range(n):
                        res[i][j] = (res[i][j] + val * B[k][j]) % MOD
            return res 

        def power(A,m):
            n = len(A)
            res = [[0]*n for _ in range(n)]
            for i in range(n):
                res[i][i] = 1

            while m:
                if(m%2):
                    res = matrix_mul(res,A)
                A = matrix_mul(A,A)
                m//=2
            return res 

        
        U = power(U,n-1)
        dp = [[1]*2*k]
        dp = matrix_mul(dp,U)
        
        ans = 0
        for i in range(2*k):
            ans+=dp[0][i]
            ans%=MOD
        return ans


# time complexity: O(k^3*log(n))
# space complexity: O(k^2)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))