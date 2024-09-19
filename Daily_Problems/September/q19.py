from typing import List,Optional
from collections import deque, defaultdict
import sys, math, heapq

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if(expression.isdigit()):
            return [int(expression)]

        ans = []
        for i in range(len(expression)):
            ch = expression[i]
            if ch in '+-*':
                left_ans = self.diffWaysToCompute(expression[:i]) 
                right_ans = self.diffWaysToCompute(expression[i+1:])
                
                for l in left_ans:
                    for r in right_ans:
                        if(ch=='+'):ans.append(l+r)
                        elif(ch=='-'):ans.append(l-r)
                        elif(ch=='*'):ans.append(l*r)
        
        return ans
            
# time complexity: O(n*2^n)
# space complexity: O(n)
if __name__ == "__main__":
    for _ in range(int(input().strip())):
        n = int(input().strip())
        arr = list(map(int,input().strip().split()))
        print(Solution().func(arr,n))