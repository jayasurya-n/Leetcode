from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq, bisect
from itertools import permutations

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        a,b,c,d = cards
        INF = 10**20

        def _value(a,b,op):
            if(op=='+'):return a+b
            if(op=='-'):return a-b
            if(op=='*'):return a*b
            if(op=='/'):return a/b if b!=0 else INF

        def solve(a,b,c,d):
            operations = ['+','-','*','/']
            for op1 in operations:
                for op2 in operations:
                    for op3 in operations:
                        # (a op1 b) op2 (c op3 d)
                        exp1 = _value(a,b,op1)
                        exp2 = _value(c,d,op3)
                        if(exp1!=INF and exp2!=INF):
                            exp3 = _value(exp1,exp2,op2)
                            if(abs(exp3-24) < 1e-6):return True

                        # (a op1 (b op2 (c op3 d))
                        exp1 = _value(c,d,op3)
                        if(exp1!=INF):
                            exp2 = _value(b,exp1,op2)
                            if(exp2!=INF):
                                exp3 = _value(a,exp2,op1)
                                if(abs(exp3-24) < 1e-6):return True

                        # (a op1 ((b op2 c) op3 d))
                        exp1 = _value(b,c,op2)
                        if(exp1!=INF):
                            exp2 = _value(exp1,d,op3)
                            if(exp2!=INF):
                                exp3 = _value(a,exp2,op1)
                                if(abs(exp3-24) < 1e-6):return True
            return False

        for p in permutations([a,b,c,d]):
            a,b,c,d = p
            if(solve(a,b,c,d)):return True
        return False
    
# time complexity: O(24*n^3)
# space complexity: O(1)
if __name__ == "__main__":
    for _ in range(ii()):
        n = ii()
        arr = lii()
        print(Solution().func(arr,n))