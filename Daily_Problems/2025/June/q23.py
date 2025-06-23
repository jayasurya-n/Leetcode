
from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        # q = deque([[]])
        # ans = 0

        # def check(num_string):
        #     l = len(num_string)
        #     num = 0
        #     for i in range(l):
        #         num+=k**(l-1-i)*int(num_string[i])

        #     return str(num)==str(num)[::-1],num
            
        # n+=1
        # while n>0:
        #     num_string = q.popleft()
        #     if(num_string==['0']):continue
        #     l = len(num_string) 
        #     if(l%2==1):
        #         half = num_string[:(l+1)//2]
        #         new = half+half[::-1]
        #         q.append(new)
        #         bool,num = check(new)
        #         if(bool):
        #             ans+=num
        #             n-=1
        #         if(n==0):break
        #     else:
        #         half = num_string[:l//2]
        #         for middle in range(k):
        #             new = half+[str(middle)]+half[::-1]
        #             q.append(new)
        #             bool,num = check(new) 
        #             if(bool):
        #                 ans+=num
        #                 n-=1
        #             if(n==0):break

        # return ans

        ans = 0
        start = 1

        def check(num):
            k_binary = []
            while num:
                k_binary.append(num%k)
                num//=k
            return k_binary==k_binary[::-1] 

        while n>0:
            for op in [0,1]:
                if(n==0):break
                for num in range(start,10*start):
                    new = temp = num
                    if(op==0):temp//=10
                    while temp:
                        new*=10
                        new+=temp%10
                        temp//=10
                    
                    if(check(new)):
                        ans+=new
                        n-=1
                    if(n==0):break
            start*=10

        return ans
                    
# time complexity: O()
# space complexity: O()
if __name__ == "__main__":
    for _ in range(ii()):
        k,n = lii()
        print(Solution().kMirror(k,n))