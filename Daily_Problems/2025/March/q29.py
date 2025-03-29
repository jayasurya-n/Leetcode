from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def sieve_prime_factorisation(n):
    # O(nloglogn)
    # least prime factor
    lp = list(range(n+1))
    lp[0] = lp[1] = -1
    for i in range(2,int(n**0.5)+1):
        if(lp[i]==i):
            for j in range(i*i,n+1,i):
                if(lp[j]==j):lp[j] = i
    return lp

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mod = 10**9+7
        
        score = [0]*n
        maxi = max(nums)
        lp = sieve_prime_factorisation(maxi)
        for i,num in enumerate(nums):
            count = set()
            while(num!=1):
                p = lp[num]
                num//=p
                count.add(p)
            score[i] = len(count)
        
        pge = [-1]*n        
        stack = []
        for i in range(n):
            while(stack and score[stack[-1]]<score[i]):stack.pop()
            pge[i] = stack[-1] if stack else -1
            stack.append(i)

        nge = [n]*n
        stack = []
        for i in range(n-1,-1,-1):
            while(stack and score[stack[-1]]<=score[i]):stack.pop()
            nge[i] = stack[-1] if stack else n
            stack.append(i)

        sorted_nums = [(nums[i],(i-pge[i])*(nge[i]-i)) for i in range(n)]
        sorted_nums.sort(reverse=True)
        
        ans = 1
        for i in range(n):
            num,cnt = sorted_nums[i]
            if(k<=cnt):
                ans*=pow(num,k,mod)
                ans%=mod
                k = 0
                break
            
            ans*=pow(num,cnt,mod)
            ans%=mod
            k-=cnt
        return ans
                
# time complexity: O(n(logn+logm)+mloglogm)
# space complexity: O(n+m)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))